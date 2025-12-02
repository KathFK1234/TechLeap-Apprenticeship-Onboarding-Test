from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

class User(BaseModel):
    name: str
    email: str
    password: str

class RSVP(BaseModel):
    event: str
    eventID: int
    attending: bool

users = []

@router.post("/users")
def new_user(user: User):
    users.append(user)
    # print(users)
    return users

@router.get("/users")
def list_users(limit: int = 5):
    print(users[0:limit])
    return users[0:limit]

@router.get("/users/{userID}")
def get_userName(userID: int):
    userName = users[userID]
    if userID < len(users):
        print(userName)
        return userName
    else:
        raise HTTPException(status_code=400, detail="User not found")

# @router.post("/events/{eventID}/RSVP")
# def event_RSVP():
