"""
app.py - Main module for the Golden Leaves App

This module initializes the Flask application, sets up core routes,
and handles the configuration of extensions such as database connections and authentication.
The primary purpose of this file is to serve as the entry point for the backend service.

"""
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)


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
    return "It's fine... Everything is fine..."


if __name__ == '__main__':
    app.run(debug=True)
