from fastapi import FastAPI
from pydantic import BaseModel
from routers import users, organizers, events

app = FastAPI()

# class User(BaseModel):
#     name: str
#     email: str

app.include_router(users.router)
app.include_router(organizers.router)
app.include_router(events.router)