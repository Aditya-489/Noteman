import sqlite3 as sql
def get_db_connection():
    try:
        conn=sql.connect("notes.db")
        return conn
    except sql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def init_db():
    conn=get_db_connection()
    if conn is not None:
        try:
            with conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL
                    )
                ''')
        except sql.Error as e:
            print(f"Error initializing the database: {e}")
        finally:
            conn.close()