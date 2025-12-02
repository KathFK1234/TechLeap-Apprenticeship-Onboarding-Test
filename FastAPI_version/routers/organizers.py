from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/organizers", tags=["organizers"])

# To create and list organizers in system
class Organizer(BaseModel):
    name: str
    email: str
    password: str

organizers = []

@router.post("/organizers")
def new_user(organizer: Organizer):
    organizers.append(organizer)
    # print(organizers)
    return organizers

@router.get("/organizers")
def list_users(limit: int = 5):
    print(organizers[0:limit])
    return organizers[0:limit]

