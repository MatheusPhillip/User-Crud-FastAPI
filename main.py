from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest

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

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            deleted_user = user
            db.remove(user)
            return {"message": "user deleted", "user": deleted_user}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "user updated"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
        