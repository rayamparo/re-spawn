from src.app import app
from flask import request, Response, redirect, render_template, make_response, jsonify
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
    if user_id == 'Wrong credentials':
        return Response('Invalid credentials', status=401)
    return dumps(user_id, cls=UserEncoder)