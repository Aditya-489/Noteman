from db import get_db_connection
from fastapi import APIRouter
router =APIRouter(prefix="/remove")

@router.delete("/")
def remove_note(note_id:int=None,note_title:str=None) -> None:
    conn=get_db_connection()
    cur=conn.cursor()
    try:
        if note_id is not None:
            cur.execute("delete from notes where id=%s",(note_id,))
            conn.commit()
            print("removed note ",note_id)
        elif note_title is not None:
            cur.execute("delete from notes where title=%s",(note_title,))
            conn.commit()
            print("removed note ",note_title)
        else:
            print("Please provide either note_id or note_title")
            return
    except Exception as e:
        print(f"Error removing note: {e}")
    finally: 
        cur.close()       
        conn.close()