from src.utils.db import db_connection

#GET all user's games
def get_users_games(user_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM games WHERE owner_id = %s", (user_id,))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()

#POST new game into user's library
def post_game(user_id, game_id, game_name, game_release_date, game_summary, game_status, game_list):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO games (owner_id, game_id, game_name, game_release_date, game_summary, game_status, game_list) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, game_id, game_name, game_release_date, game_summary, game_status, game_list))
        con.commit()
    finally:
        con.close()

#GET check if game already exists in user's account
def get_users_game_by_id(user_id, game_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM games WHERE owner_id = %s AND game_id = %s", (user_id, game_id))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()

#DELETE game from user's library
def remove_game(user_id, game_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM games WHERE owner_id = %s AND game_id = %s", (user_id, game_id))
        con.commit()
    finally:
        con.close()

#GET all games by for user by list name
def get_games_by_list(user_id, list_name):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM games WHERE owner_id = %s AND game_list = %s", (user_id, list_name))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()