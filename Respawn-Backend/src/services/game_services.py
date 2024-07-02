import src.dao.game_dao as game_dao
from src.models.game_model import Game

#GET all user's games
def get_users_games(user_id):
    users_games = game_dao.get_users_games(user_id)
    users_games_list = []
    count = 0
    if len(users_games) > 0:
        for game in users_games:
            users_games_list.insert(count, Game(game[0], game[1], game[2], str(game[3]), game[4], game[5], game[6]))
            count + 1
        return users_games_list
