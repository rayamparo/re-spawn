import src.dao.lists_dao as lists_dao

#GET users lists
def get_users_list(user_id):
    users_list = lists_dao.get_users_lists(user_id)
    return users_list

def get_list_by_name(list_name):
    lists_dao.get_list_by_name(list_name)

#POST new user list
def post_new_list(user_id, list_name):
    if len(list_name) < 1:
        return 'Please enter at least one character'
    lists_dao.post_new_lists(user_id, list_name)
    check_list = lists_dao.get_list_by_name(list_name)
    print(check_list)
    return 'working'