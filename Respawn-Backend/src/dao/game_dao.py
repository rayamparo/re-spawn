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