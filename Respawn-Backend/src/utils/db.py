import psycopg2
import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connection to DB
def db_connection():
    host = os.getenv('dev_host')
    database = os.getenv('dev_database')
    user = os.getenv('dev_user')
    password = os.getenv('dev_password')
    return psycopg2.connect(
        host = f'{host}',
        database = f'{database}',
        user = f'{user}',
        password = f'{password}'
    )