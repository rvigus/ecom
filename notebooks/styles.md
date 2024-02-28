## Generating a product catalog


```python
from faker import Faker
import pandas as pd
import random
import string
import numpy as np
import hashlib
import faker
fake = faker.Faker()
```


```python
product_categories = [
    "Knitwear", 
    "T-Shirts", 
    "Jeans", 
    "Shorts", 
    "Shoes", 
    "Trousers", 
    "Tailoring", 
    "Accessories",
    "Jackets",
    "Shirts",
    "Sweatshirts"
]

genders = [
    "Men", 
    "Women"
]

colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Pink",
    "Orange",
    "Purple",
    "Grey",
    "Teal",
    "Maroon",
    "Navy",
    "Olive",
    "Magenta",
    "Lime",
    "Crimson",
    "Beige",
    "Turquoise",
    "Silver"
]

standard_sizes = [
    "XS",  
    "S",   
    "M",   
    "L",   
    "XL",  
    "XXL", 
]

product_categories_materials = {
    "Knitwear": ["Wool", "Cotton", "Cashmere", "Acrylic", "Bamboo"],
    "T-Shirts": ["Cotton", "Polyester", "Rayon", "Linen", "Bamboo"],
    "Jeans": ["Denim", "Cotton", "Elastane", "Polyester", "Corduroy"],
    "Shorts": ["Cotton", "Polyester", "Denim", "Nylon", "Linen", "Corduroy"],
    "Shoes": ["Leather", "Suede", "Canvas", "Synthetic", "Rubber"],
    "Trousers": ["Cotton", "Wool", "Polyester", "Linen", "Viscose", "Corduroy", "Suede"],
    "Tailoring": ["Wool", "Polyester", "Silk", "Linen", "Cotton", "Corduroy"],
    "Accessories": ["Leather", "Silk", "Cotton", "Wool", "Synthetic", "Suede"],
    "Jackets": ["Leather", "Denim", "Polyester", "Cotton", "Nylon", "Corduroy", "Suede"],
    "Shirts": ["Cotton", "Linen", "Polyester", "Silk", "Rayon", "Corduroy"],
    "Sweatshirts": ["Cotton", "Polyester", "Fleece", "Wool", "Bamboo"]
}


subcategories = {
    "Knitwear": [
        "Cardigans", "Pullovers", "Sweater Vests", "Turtlenecks", "Chunky Knits", "Fine Knit Sweaters"
    ],
    "T-Shirts": [
        "Graphic Tees", "Plain Tees", "Long Sleeve Tees", "Polo Shirts", "Henley Shirts", "Crew Neck T-Shirts", "V-Neck T-Shirts"
    ],
    "Jeans": [
        "Skinny Jeans", "Straight Leg Jeans", "Bootcut Jeans", "High-Waisted Jeans", "Distressed Jeans", "Slim Fit Jeans"
    ],
    "Shorts": [
        "Denim Shorts", "Chino Shorts", "Cargo Shorts", "Bermuda Shorts", "Athletic Shorts", "Board Shorts", "Leather Shorts"
    ],
    "Shoes": [
        "Sneakers", "Dress Shoes", "Boots", "Sandals", "Loafers", "Running Shoes", "Oxfords", "Derbys"
    ],
    "Trousers": [
        "Chinos", "Dress Pants", "Cargo Pants", "Slim Fit Trousers", "Wide-Leg Trousers", "Joggers", "Cropped Trousers"
    ],
    "Tailoring": [
        "Suits", "Blazers", "Dress Shirts", "Tuxedos", "Vests", "Tailored Jackets", "Morning Coats"
    ],
    "Accessories": [
        "Hats", "Bags", "Belts", "Scarves", "Sunglasses", "Watches", "Jewelry", "Ties", "Wallets", "Cufflinks"
    ],
    "Jackets": [
        "Bomber Jackets", "Denim Jackets", "Leather Jackets", "Parkas", "Blazers", "Windbreakers", "Puffer Jackets"
    ],
    "Shirts": [
        "Dress Shirts", "Casual Shirts", "Flannel Shirts", "Oxford Shirts", "Hawaiian Shirts", "Chambray Shirts", "Linen Shirts"
    ],
    "Sweatshirts": [
        "Hoodies", "Crew Neck Sweatshirts", "Zip-Up Sweatshirts", "Oversized Sweatshirts", "Graphic Sweatshirts", "Fleece Sweatshirts"
    ]
}

```


```python
def generate_price(category):
    """
    Generates prices for different product categories
    """
    price_ranges = {
        "Knitwear": (25, 100),
        "T-Shirts": (15, 50),
        "Jeans": (40, 120),
        "Shorts": (20, 60),
        "Shoes": (50, 200),
        "Trousers": (30, 100),
        "Tailoring": (100, 300),
        "Accessories": (10, 70),
        "Jackets": (60, 250),
        "Shirts": (25, 80),
        "Sweatshirts": (30, 90),
    }
    
    lower_bound, upper_bound = price_ranges.get(category)
    # Generate a random price within the range
    price = round(random.uniform(lower_bound, upper_bound), 0)
    return price
```


```python
def generate_alphanumeric_id(length):
    """
    Generate an random alphanumeric id
    """
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for i in range(length))
    return random_id.upper()
```


```python
# First we need to build our catalog of products
n_products = 1000

styles = []
for i in range(n_products):
    category = random.choice(product_categories)
    gender = random.choice(genders)
    material = random.choice(product_categories_materials.get(category))
    sub_category = random.choice(subcategories.get(category))
    name = (fake.name()).split(' ')[1]
    price = generate_price(category)
    
    styles.append(
        {"gender":gender, 
         "category":category, 
         "sub_category":sub_category, 
         "material": material, 
         "name": name,
         "price": price
        })

df_style = pd.DataFrame(styles)
df_style["style_id"] = [generate_alphanumeric_id(10) for i in range(len(df_style))]
```


```python
print(df_style.head())
```

      gender     category      sub_category material       name  price    style_id
    0    Men  Accessories           Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ
    1  Women      Jackets     Denim Jackets   Cotton     Gordon  166.0  DULQGXZB5Y
    2    Men  Accessories           Scarves    Suede     Brenda   54.0  NMIQ4ST5KM
    3  Women     T-Shirts  Long Sleeve Tees   Bamboo   Thompson   48.0  0OTCPPDLE2
    4    Men       Shorts    Bermuda Shorts    Nylon      Riley   20.0  PROGZGEDKD



```python
# products come in different colors, these we'll call styleoptions
styleoptions = []

for index, row in df_style.iterrows():
    _colors = colors.copy()

    n_colors = random.randint(2, 8)
    for c in range(n_colors):
        color = random.choice(_colors)
        _colors.remove(color)

        row_dict = row.to_dict()
        row_dict['color'] = color
        styleoptions.append(row_dict)
        
df_styleoption = pd.DataFrame(styleoptions)
df_styleoption["style_option_id"] = df_styleoption['style_id'] + '_' + df_styleoption['color'].str.upper()
```


```python
print(df_styleoption.head())
```

      gender     category   sub_category material       name  price    style_id  \
    0    Men  Accessories        Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    1    Men  Accessories        Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    2    Men  Accessories        Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    3    Men  Accessories        Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    4  Women      Jackets  Denim Jackets   Cotton     Gordon  166.0  DULQGXZB5Y   
    
         color     style_option_id  
    0   Maroon   XR7NUURBHJ_MAROON  
    1    Black    XR7NUURBHJ_BLACK  
    2      Red      XR7NUURBHJ_RED  
    3     Grey     XR7NUURBHJ_GREY  
    4  Magenta  DULQGXZB5Y_MAGENTA  



```python
# Now we need to generate the SKU itself, which is the specific size of a styleoption. 
# For simplicity, lets assume there are always all sizes available.
skus = []

for index, row in df_styleoption.iterrows():
    for s in standard_sizes:
        row_dict = row.to_dict()
        row_dict['size'] = s
        skus.append(row_dict)
        
df_sku = pd.DataFrame(skus)
df_sku["sku_id"] = df_sku['style_option_id'] + '_' + df_sku['size'].str.upper()
```


```python
print(df_sku.head())
```

      gender     category sub_category material       name  price    style_id  \
    0    Men  Accessories      Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    1    Men  Accessories      Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    2    Men  Accessories      Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    3    Men  Accessories      Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    4    Men  Accessories      Wallets     Silk  Gutierrez   37.0  XR7NUURBHJ   
    
        color    style_option_id size                sku_id  
    0  Maroon  XR7NUURBHJ_MAROON   XS  XR7NUURBHJ_MAROON_XS  
    1  Maroon  XR7NUURBHJ_MAROON    S   XR7NUURBHJ_MAROON_S  
    2  Maroon  XR7NUURBHJ_MAROON    M   XR7NUURBHJ_MAROON_M  
    3  Maroon  XR7NUURBHJ_MAROON    L   XR7NUURBHJ_MAROON_L  
    4  Maroon  XR7NUURBHJ_MAROON   XL  XR7NUURBHJ_MAROON_XL  



```python
print(len(df_sku), len(df_styleoption), len(df_style))
```

    29754 4959 1000



```python
df_style.to_csv("styles.csv", sep=";", index=None)
df_styleoption.to_csv("styleoptions.csv", sep=";", index=None)
df_sku.to_csv("skus.csv", sep=';', index=None)
```
