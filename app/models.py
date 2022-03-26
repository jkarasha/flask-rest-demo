from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  phone_number = db.Column(db.String(80))
  email_address = db.Column(db.String(80))
  pin_number = db.Column(db.String(80))
  county = db.Column(db.String(80))
  city = db.Column(db.String(80))
  state = db.Column(db.String(80))
  zip_code = db.Column(db.String(80))

