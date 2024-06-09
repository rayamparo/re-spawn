import src.dao.user_dao as user_dao
from src.models.user_model import User

#Gets user via ID
def get_user_by_id(user_id):
    # user_dict = {}
    user = user_dao.get_user(user_id)
    if user == []:
        return {}
    return User(user[0][0], user[0][1], user[0][2], user[0][3], 0, 0)
    # return user_dict