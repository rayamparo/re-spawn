import src.dao.game_dao as game_dao

#GET all user's games
def get_users_games(user_id):
    users_games = game_dao.get_users_games(user_id)
