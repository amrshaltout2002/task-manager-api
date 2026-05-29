from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import auth, users
from app.models import User, Task

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message":"Task Manager API is running right now"}

Base.metadata.create_all(bind=engine)
