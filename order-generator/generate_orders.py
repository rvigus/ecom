import json
import random
from datetime import datetime
from time import sleep

import boto3
import pandas as pd
from faker import Faker

# Init faker
fake = Faker()


# Configure S3
s3 = boto3.client('s3',
                  endpoint_url='http://localstack:4566',
                  aws_access_key_id='test',
                  aws_secret_access_key='test',
                  region_name='us-east-1')

bucket_name = 'data'
prefix = "orders"

def load_product_catalog():
    return pd.read_csv("./data/skus.csv", sep=';')

def get_discount_rate(lower, upper, multiple):
    random_int = random.randint(lower, int(upper / multiple))
    return random_int * multiple

def get_discount_value(price, quantity, discount_rate):
    return price * quantity * discount_rate

def get_payment_method():
    method = [
        "PayPal",
        "Visa",
        "Mastercard",
        "American Express",
        "Apple Pay",
        "Google Pay",
        "Amazon Pay",
        "Klarna"
    ]
    return random.choice(method)

def get_shipping_method():
    shipping = [
        "standard",
        "express",
        "next day",
    ]
    return random.choices(shipping, weights=[0.80, 0.15, 0.05], k=1)[0]


def generate_order(seed_df):

    sku_id = random.choice(seed_df['sku_id'].to_list())
    price = seed_df[seed_df['sku_id'] == sku_id]['price'].iat[0]
    quantity = random.randint(1, 10)
    discount_rate = get_discount_rate(0, 0.6, 0.05)
    discount_value = get_discount_value(price, quantity, discount_rate)
    order_status = random.choices(['success', 'cancelled'], weights=[0.95, 0.05], k=1)[0]

    order = {
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "customer_email": fake.email(),
        "customer_address": fake.address(),
        "order_ts": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "sku_id": sku_id,
        "quantity": quantity,
        "price": price,
        "total": price * quantity,
        "discount_rate": discount_rate,
        "discounted_price": price * (1-discount_rate),
        "discount_value": discount_value,
        "order_status": order_status,
        "payment_method": get_payment_method(),
        "shipping_method": get_shipping_method()
    }
    return json.dumps(order)

def upload_to_s3(order_data):

    j = json.loads(order_data)
    order_id = j['order_id']
    order_dt = j["order_ts"][:10]

    s3_path = f"{prefix}/dt={order_dt}/order_{order_id}.json"
    s3.put_object(Bucket=bucket_name, Key=s3_path, Body=order_data)
    print(f"Uploaded order {order_id} to S3 bucket {bucket_name}/{s3_path}.")


if __name__ == "__main__":
    skus = load_product_catalog()
    while True:
        order_data = generate_order(skus)
        upload_to_s3(order_data)
        print(order_data, flush=True)
        sleep(random.randint(1, 10))
