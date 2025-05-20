import sqlite3
from sqlite3 import Error

db_file = "library_database.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database (version {sqlite3.version})")
        return conn
    except Error as e:
        print(e)
    
    return conn
def close_connection(conn):
    if conn:
        conn.close()
        print("SQLite connection is closed")