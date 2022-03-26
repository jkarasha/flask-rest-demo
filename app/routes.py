from app import app
from flask import jsonify
from app.models import User
from app.schemas import UserSchema

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/users/<int:id>', methods=['GET', 'POST'])
def get_user(id):
    user = User.query.get_or_404(id)
    #
    user_schema = UserSchema()
    result = user_schema.dump(user)
    #
    return {'user': result}

@app.route('/users')
def get_users():
    users = User.query.all()
    #
    users_schema = UserSchema(many=True)
    result = users_schema.dump(users)
    #
    return {'users': result}

@app.route('/users/<int:id>/name', methods=['GET', 'POST'])
def get_user_name_by_id(id):
    user = User.query.get_or_404(id)
    #
    user_name_schema = UserSchema(only=("first_name", "last_name"))
    result = user_name_schema.dump(user)
    #
    return {'user': result}

@app.route('/users/<int:id>/pin', methods=['GET', 'POST'])
def get_user_pin(id):
    user = User.query.get_or_404(id)
    #
    user_pin_schema = UserSchema(only=("id", "pin_number"))
    result = user_pin_schema.dump(user)
    #
    return {'user': result}

@app.route('/users/<string:phone_number>/name', methods=['GET', 'POST'])
def get_user_name_by_phone(phone_number):
    user = User.query.filter_by(phone_number=phone_number).first_or_404()
    #
    user_pin_schema = UserSchema(only=("first_name", "last_name"))
    result = user_pin_schema.dump(user)
    #
    return {'user': result}