"""
Configuration Settings.
"""
import os

class Config():
    """Config object for secret keys."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'