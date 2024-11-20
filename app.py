"""
app.py - Main module for the Golden Leaves App

This module initializes the Flask application, sets up core routes,
and handles the configuration of extensions such as database connections and authentication.
The primary purpose of this file is to serve as the entry point for the backend service.

"""
import os
import redis
import psycopg2
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

redis_client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=os.getenv('REDIS_PORT', 6379),  # type: ignore
    decode_responses=True
)

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "mydatabase"),
    user=os.getenv("POSTGRES_USER", "myuser"),
    password=os.getenv("POSTGRES_PASSWORD", "mypassword"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", 5432),
)


@app.get("/")
def index():
    """
    Home endpoint that returns a simple welcome message.

    This function serves as a basic health check for the API.
    It returns a "Hello, World!" message to verify that the 
    Flask application is running.

    Returns:
        str: A welcome message.
    """
    redis_client.set("message", 'Hello from Redis!')
    message = redis_client.get("message")

    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    db_time = cur.fetchone()
    return f"{message}, PostgreSQL Time: {db_time}"


if __name__ == '__main__':
    app.run(debug=True)
