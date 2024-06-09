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