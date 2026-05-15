
from db import get_db_connection
from fastapi import APIRouter

router=APIRouter(prefix="/create")

@router.post("/")
def create_note(title:str ,content :str) -> None:
        conn=get_db_connection()
        if conn is None:
                print("Failed to connect to DB")
                return
        cur =conn.cursor()
        cur.execute("INSERT INTO NOTES (title,value) VALUES(%s,%s)",(title,content))
        conn.commit()


            