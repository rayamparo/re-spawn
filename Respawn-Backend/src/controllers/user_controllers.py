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