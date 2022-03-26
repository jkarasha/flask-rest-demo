import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
  SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
