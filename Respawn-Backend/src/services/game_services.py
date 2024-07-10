import src.dao.game_dao as game_dao
from src.models.game_model import Game
import src.services.lists_services as lists_services
from datetime import datetime

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

#POST new game into user's list
def post_game(user_id, game_id, game_name, game_release_date, game_summary, game_status, game_list):
    game_exists = get_users_game_by_id(user_id, game_id)
    if game_exists == 'Game does not exist in user\'s account':
        if game_list != '':
            check_if_list_exists = lists_services.get_list_by_name(user_id, game_list)
            if check_if_list_exists != []:
                date_str = f"{game_release_date} 00:00:00"
                date_format = '%Y-%m-%d %H:%M:%S'
                date_obj = datetime.strptime(date_str, date_format)
                game_dao.post_game(user_id, game_id, game_name, date_obj, game_summary, game_status, game_list)
                game_check = get_users_game_by_id(user_id, game_id)
                if game_check == 'Game already exists in user\'s account':
                    return 'Successfully added game.'
                else:
                    return 'Game was not added to library, please try again.'
            else:
                return 'Game was not added to library, please try again.'
        else:
            date_str = f"{game_release_date} 00:00:00"
            date_format = '%Y-%m-%d %H:%M:%S'
            date_obj = datetime.strptime(date_str, date_format)
            game_dao.post_game(user_id, game_id, game_name, date_obj, game_summary, game_status, game_list)
            game_check = get_users_game_by_id(user_id, game_id)
            if game_check == 'Game already exists in user\'s account':
                return 'Successfully added game.'
            else:
                return 'Game was not added to library, please try again.'
    else:
        return 'Game already exists in user\'s account'

#GET users game by ID to check if game already exists on the user's account
def get_users_game_by_id(user_id, game_id):
    game = game_dao.get_users_game_by_id(user_id, game_id)
    if game == []:
        return 'Game does not exist in user\'s account'
    else:
        return 'Game already exists in user\'s account'

#DELETE game from user's library
def remove_game(user_id, game_id):
    game_dao.remove_game(user_id, game_id)

#GET all games with a list name
def get_games_by_list(user_id, list_name):
    games_by_list_name = game_dao.get_games_by_list(user_id, list_name)
    users_games_list = []
    count = 0
    if len(games_by_list_name) > 0:
        for game in games_by_list_name:
            users_games_list.insert(count, Game(game[0], game[1], game[2], str(game[3]), game[4], game[5], game[6]))
            count + 1
    return users_games_list