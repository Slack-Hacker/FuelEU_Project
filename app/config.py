import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fuel_eu.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
