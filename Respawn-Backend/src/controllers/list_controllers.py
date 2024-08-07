from src.app import app
from flask import request, Response
from json import dumps
from src.models.user_model import UserEncoder
import src.services.user_services as user_services
import src.services.lists_services as lists_services

@app.route('/users/<int:user_id>/lists', methods=['GET', 'POST', 'PUT'])
def post_or_get_users_lists(user_id):
    #GET all lists associated with user
    if request.method == 'GET':
        if user_services.get_user_by_id(user_id) == {}:
            return Response('No such user exists', status=404)
        users_lists = lists_services.get_users_lists(user_id)
        return dumps(users_lists, cls=UserEncoder)
    #POST a new list
    if request.method == 'POST':
        req_body = request.get_json()
        list_name = req_body['list_name']
        posted_list = lists_services.post_new_list(user_id, list_name)
        if posted_list == 'List already exists.':
            return Response('List already exists.', status=409)
        elif posted_list == 'List was not created, please try again.':
            return Response('List was not created, please try again.', status=504)
        return Response('List successfully created.', status=200)
    #PUT update list name for a user's game
    if request.method == 'PUT':
        req_body = request.get_json()
        game_id = req_body['game_id']
        updated_list_name = req_body['updated_list_name']
        lists_services.update_list_for_game(user_id, game_id, updated_list_name)
        return Response('Updated game list successfully.', status=200)