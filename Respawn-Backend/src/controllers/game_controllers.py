from src.app import app
from flask import request, Response
from json import dumps
from src.models.user_model import UserEncoder
import src.services.game_services as game_services

#GET & POST users games
@app.route('/users/<int:user_id>/games', methods=['GET', 'POST', 'DELETE'])
def get_users_games(user_id):
    if request.method == 'GET':
        users_games = game_services.get_users_games(user_id)
        return dumps(users_games, cls=UserEncoder)
    if request.method == 'POST':
        req_body = request.get_json()
        game_id = req_body['game_id']
        game_name = req_body['game_name']
        game_release_date = req_body['game_release_date']
        game_summary = req_body['game_summary']
        game_status = req_body['game_status']
        game_list = req_body['game_list']
        game_posted = game_services.post_game(user_id, game_id, game_name, game_release_date, game_summary, game_status, game_list)
        if game_posted == 'Game already exists in user\'s account':
            return Response('Game already exists in user\'s account', status=409)
        elif game_posted == 'Game was not added to library, please try again.':
            return Response('Game was not added to library, please try again.', status=409)
        return Response('Successfully added game to user\'s library.', status=200)
    if request.method == 'DELETE':
        req_body = request.get_json()
        game_id = req_body['game_id']
        game_services.remove_game(user_id, game_id)
        return Response('Game successfully removed from library.', status=201)