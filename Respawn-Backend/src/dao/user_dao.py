from src.utils.db import db_connection

#Gets user
def get_user(user_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()

#Gets user ID
def get_user_id(email, password):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_email = %s AND user_password = %s", (email, password))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()

#Create new user
def create_new_user(user_email, user_password, user_gamertag):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (default, %s, %s, %s)", (user_email, user_password, user_gamertag))
        con.commit()
    finally:
        con.close()