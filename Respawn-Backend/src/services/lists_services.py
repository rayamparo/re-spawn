import src.dao.lists_dao as lists_dao

#GET users lists
def get_users_lists(user_id):
    users_list = lists_dao.get_users_lists(user_id)
    lists_dict = {}
    count = 0
    for list in users_list:
        count = count + 1
        lists_dict[count] = list[2]
    return lists_dict

#GET a list by name
def get_list_by_name(user_id, list_name):
    lists_dao.get_list_by_name(user_id, list_name)

#POST new user list
def post_new_list(user_id, list_name):
    if len(list_name) < 1:
        return 'Please enter at least one character.'
    check_if_list_exists = lists_dao.get_list_by_name(user_id, list_name)
    if check_if_list_exists != []:
        return 'List already exists.'
    lists_dao.post_new_list(user_id, list_name)
    check_list = lists_dao.get_list_by_name(user_id, list_name)
    if check_list == []:
        return 'List was not created, please try again.'
    return 'List successfully created.'

def update_list_for_game(user_id, game_id, updated_list_name):
    lists_dao.update_list_name(user_id, game_id, updated_list_name)
    return 'Updated game list successfully.'