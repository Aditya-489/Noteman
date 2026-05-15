from noteman.db import get_db_connection

def list_all() -> None:
        conn=get_db_connection()
        try:
                if conn is None:
                        print("Failed to connect to DB")
                        return
                cur =conn.cursor()
                cur.execute("SELECT * FROM NOTES")
                rows=cur.fetchall()
                for row in rows:
                        print(f"ID: {row[0]}, title: {row[1]}, value: {row[2]}")
        except Exception as e:
                print(f"Error fetching notes: {e}")
        finally:   
                cur.close()             
                conn.close()
        
def get_note(note_id:int=None,note_title :str=None) ->None:
        conn=get_db_connection()
        cur=conn.cursor()
        try:
                if note_id is not None:
                        cur.execute("select title,value from notes where id=%s",(note_id,))
                        row=cur.fetchone()
                        if row:
                                print(row)
                        else:
                                print("Note not found")
                elif note_title is not None:
                        cur.execute("select title,value from notes where title=%s",(note_title,))
                        row=cur.fetchone()
                        if row:
                                print(row)
                        else:
                                print("Note not found")
                else :
                        print("Please provide either note_id or note_title")
                        return
        except Exception as e:
                print(f"Error fetching note: {e}")
        finally:
                cur.close()
                conn.close()