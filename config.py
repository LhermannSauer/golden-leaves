"""
Basic Configuration File.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = os.getenv('REDIS_URL')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


# Configuration mapping
config_by_name = {  # type: ignore
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
