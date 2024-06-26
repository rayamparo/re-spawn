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