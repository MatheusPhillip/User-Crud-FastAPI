from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Matheus", 
        last_name="Miranda",
        gender=Gender.male,
        roles=[Role.user, Role.admin]
    ),
    User(
        id=uuid4(), 
        first_name="Ana", 
        last_name="Silva",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(), 
        first_name="Priscilla", 
        last_name="Santana",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(), 
        first_name="Hadja", 
        last_name="Costa",
        gender=Gender.female,
        roles=[Role.student]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}