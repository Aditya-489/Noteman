import psycopg as psy
from dotenv import load_dotenv
import os
load_dotenv()

def get_db_connection():
    try:
        return psy.connect(
            host="localhost",
            port=5432,
            dbname="notes",
            user="YOUR_USERNAME",
            password="YOUR_PASSWORD"
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None