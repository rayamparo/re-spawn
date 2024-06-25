from src.app import app
from flask import request, Response
from json import dumps
from src.models.user_model import UserEncoder
import src.services.game_services as game_services

#GET users games
@app.route('/games/<int:user_id>/games', methods=['GET'])
def get_users_games(user_id):
    users_games = game_services.get_users_games(user_id)