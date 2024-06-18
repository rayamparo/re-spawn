from src.utils.db import db_connection

#GET user's lists
def get_users_lists(user_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM lists WHERE owner_id = %s", (user_id,))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()

#POST new list for user
def post_new_list(user_id, list_name):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO lists (owner_id, list_id, list_name) VALUES (%s, default, %s)", (user_id, list_name))
        con.commit()
    finally:
        con.close()

#GET list by name
def get_list_by_name(user_id, list_name):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM lists WHERE owner_id = %s AND list_name = %s", (user_id, list_name))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()