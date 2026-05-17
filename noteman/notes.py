
from noteman.db import get_db_connection


def create_note(title:str ,content :str) -> None:
        conn=get_db_connection()
        if conn is None:
                print("Failed to connect to DB")
                return
        cur =conn.cursor()
        cur.execute("INSERT INTO NOTES (title,content) VALUES(?,?)",(title,content))
        conn.commit()


            