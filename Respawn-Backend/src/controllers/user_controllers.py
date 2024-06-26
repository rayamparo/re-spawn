from src.app import app
from flask import request, Response
from json import dumps
from src.models.user_model import UserEncoder
import src.services.user_services as user_services

#Gets user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_services.get_user_by_id(user_id)
    if user == {}:
        return Response('User does not exist', status=404)
    return dumps(user, cls=UserEncoder)

#User login (returns id, fethces the user from the front-end into route above to fetch data for user dashboard)
@app.route('/users/login', methods=['POST'])
def user_login():
    req_body = request.get_json()
    email = req_body['email']
    password = req_body['password']
    user_id = user_services.get_user_id(email, password)
    if user_id == 'Wrong credentials.':
        return Response('Invalid credentials.', status=401)
    return dumps(user_id, cls=UserEncoder)

# POST new user
@app.route('/users/register', methods=['POST'])
def user_register():
    req_body = request.get_json()
    email = req_body['email']
    password = req_body['password']
    gamertag = req_body['gamertag']
    created_user = user_services.create_user(email, password, gamertag)
    if created_user == 'User already exists.':
        return Response('User already exists.', status=409)
    if created_user == 'User not created, please try again.':
        return Response('User not created, please try again.', status=504)
    return Response('User successfully created.', status=201)
