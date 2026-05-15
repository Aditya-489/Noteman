from routes import notes ,gather,remove
from fastapi import FastAPI 
app=FastAPI()
app.include_router(notes.router)
app.include_router(gather.router)
app.include_router(remove.router)