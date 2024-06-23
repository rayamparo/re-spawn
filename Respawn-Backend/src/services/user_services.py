import src.dao.user_dao as user_dao
from src.models.user_model import User
import src.services.lists_services as lists_services

#Gets user via ID
def get_user_by_id(user_id):
    user = user_dao.get_user(user_id)
    if user == []:
        return {}
    users_lists = lists_services.get_users_lists(user_id)
    # Currently placing 0's for user_games_list and user_lists until I create the controllers for the games and lists
    return User(user[0][0], user[0][1], user[0][2], user[0][3], 0, users_lists)

#Gets user ID
def get_user_id(email, password):
    user_id = user_dao.get_user_id(email, password)
    if user_id == []:
        return 'Wrong credentials.'
    return user_id[0][0]

#Create new user
def create_user(email, password, gamertag):
    check_if_user_exists = get_user_id(email, password)
    if check_if_user_exists != 'Wrong credentials.':
        return 'User already exists.'
    #Create user
    user_dao.create_new_user(email, password, gamertag)
    #Check if created user is in DB
    check_for_user = get_user_id(email, password)
    if check_for_user == []:
        return 'User not created, please try again.'