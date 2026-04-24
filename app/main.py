from fastapi import FastAPI
from app.db.database import Base, engine
app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Task Manager API is running right now"}

Base.metadata.create_all(bind=engine)
