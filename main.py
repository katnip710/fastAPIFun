from fastapi import FastAPI, HTTPException
from typing import List
from models import User, FaveColour, Role
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("5f0ad2cb-5710-47da-ba0f-21eec407c519"),
        first_name= "Kat",
        last_name= "Lea",
        colour= FaveColour.yellow,
        roles= [Role.admin, Role.user]
    ),
]

@app.get("/")
async def root():
    return {"Hello": "Kat"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/vi/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code= 404,
        detail= f"user with id: {user_id} does not exist"
    )