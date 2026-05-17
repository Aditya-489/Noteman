import psycopg as psy
from dotenv import load_dotenv
load_dotenv()

def get_db_connection():
    try:
        return psy.connect(
            host="localhost",
            port=5432,
            dbname="notes",
            user="username",
            password="password"
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None