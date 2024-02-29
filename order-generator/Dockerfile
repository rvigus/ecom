FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt - using uv pip for this.
ENV VIRTUAL_ENV=/usr/local
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh
RUN /root/.cargo/bin/uv pip install --no-cache -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run generate_orders.py when the container launches
CMD ["python", "./generate_orders.py"]
