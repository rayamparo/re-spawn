from src.models.game_model import Game
from src.models.list_model import List
from json import JSONEncoder

class User:

    def __init__(self, user_id, user_email, user_password, user_gamertag, user_games_list, user_lists):
        self._user_id = user_id
        self._user_email = user_email
        self._user_password = user_password
        self._user_gamertag = user_gamertag
        self._user_games_list = user_games_list
        self._user_lists = user_lists

class UserEncoder(JSONEncoder):
    def default(self, class_obj):
        if isinstance(class_obj, User):
            return class_obj.__dict__
        elif isinstance(class_obj, Game):
            return class_obj.__dict__
        elif isinstance(class_obj, List):
            return class_obj.__dict__
        else:
            return super().default(self, class_obj)