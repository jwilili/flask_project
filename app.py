from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

import os
from datetime import datetime 


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
new_db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class User(new_db.Model):
  id = new_db.Column(new_db.Integer, primary_key=True)
  email = new_db.Column(new_db.String(100))
  firstname = new_db.Column(new_db.String(200))
  lastname = new_db.Column(new_db.String(200))
  birthdate = new_db.Column(new_db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, email, firstname, lastname, birthdate):
    self.email = email
    self.firstname = firstname
    self.lastname = lastname
    self.birthdate = birthdate

# User Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'email', 'firstname', 'lastname', 'birthdate')

# Init schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
  email = request.json['email']
  firstname = request.json['firstname']
  lastname = request.json['lastname']
  birthdate = request.json['birthdate']
  birthdate_date = datetime.strptime(birthdate, '%Y-%m-%d %H:%M:%S.%f')

  new_user = User(email, firstname, lastname, birthdate_date)

  new_db.session.add(new_user)
  new_db.session.commit()

  return user_schema.jsonify(new_user)

# Get All USers
@app.route('/users', methods=['GET'])
def get_users():
  all_users = User.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result.data)

# Get Single User
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  return user_schema.jsonify(user)

# Update a User
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
  user = User.query.get(id)

  email = request.json['email']
  firstname = request.json['firstname']
  lastname = request.json['lastname']
  birthdate = request.json['birthdate']
  birthdate_date = datetime.strptime(birthdate, '%Y-%m-%d %H:%M:%S.%f')

  user.email = email
  user.firstname = firstname
  user.lastname = lastname
  user.birthdate = birthdate_date

  new_db.session.commit()

  return user_schema.jsonify(user)

# Delete User
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
  user = User.query.get(id)
  new_db.session.delete(user)
  new_db.session.commit()

  return user_schema.jsonify(user)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
