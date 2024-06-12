import src.dao.user_dao as user_dao
from src.models.user_model import User

#Gets user via ID
def get_user_by_id(user_id):
    user = user_dao.get_user(user_id)
    if user == []:
        return {}
    # Currently placing 0's for user_games_list and user_lists until I create the controllers for the games and lists
    return User(user[0][0], user[0][1], user[0][2], user[0][3], 0, 0)

#Gets user ID
def get_user_id(email, password):
    user_id = user_dao.get_user_id(email, password)
    if user_id == []:
        return 'Wrong credentials'
    return user_id[0][0]