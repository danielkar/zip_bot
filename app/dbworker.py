import psycopg2
import config
from config import USER, PASSWORD, DB, HOST, PORT
from datetime import datetime
import time
 
"""
conn = psycopg2.connect(dbname=DB, user=USER, host=HOST, port=PORT)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS usertable (id serial PRIMARY KEY, chat_id int, login varchar(64), repository varchar(64), url varchar(256), date timestamp with time zone, state int);")
"""
 
def get_current_state(chat_id):
    try:
        with psycopg2.connect(dbname=DB, user=USER,  host=HOST, port=PORT, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT state FROM usertable WHERE chat_id={chat_id};")
                return cur.fetchone()
    except KeyError:
        return config.States.S_START.value
 
def set_state(chat_id, state):
    with psycopg2.connect(dbname=DB, user=USER,  host=HOST, port=PORT, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM usertable WHERE chat_id={ chat_id }")
                if cur.fetchone() is not None:
                    cur.execute(f"UPDATE usertable SET state = {state} WHERE chat_id={chat_id};")
                else:
                    cur.execute(f"INSERT INTO usertable (chat_id, state) VALUES ({chat_id}, {state});")
 
def intering_in_db(chat_id, column, arg):
    try:
        with psycopg2.connect(dbname=DB, user=USER,  host=HOST, port=PORT, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE usertable SET {column} = '{arg}' WHERE chat_id={chat_id};")
        return True
    except:
        with psycopg2.connect(dbname='botdb', user='postgres', host='localhost', port=5433) as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO usertable (chat_id, {column}) VALUES ({chat_id}, '{arg}') ;")
        return False
 
def get_field(chat_id, column):
    with psycopg2.connect(dbname=DB, user=USER,  host=HOST, port=PORT, password=PASSWORD) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT {column} FROM usertable WHERE chat_id={chat_id};")
            return cur.fetchone()
