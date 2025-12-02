from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/events", tags=["events"])

class Event(BaseModel):
    name: str
    date: str
    location: str

events = []

@router.post("/events")
def new_event(event: Event):
    if APIRouter(tags="organizer"):
        events.append(event)
        # print(events)
        return events
    else:
        return HTTPException(status_code=403, detail="You do not have permission to add or modify events")

@router.get("/events")
def list_events(limit: int = 15):
    print(events[0:limit])
    return events[0:limit]

@router.get("/events/{eventID}")
def get_eventName(eventID: int):
    eventName = events[eventID]
    if eventID < len(events):
        print(eventName)
        return eventName
    else:
        raise HTTPException(status_code=400, detail="Event not found")

@router.post("/events/{eventID}/RSVP")
def event_capacity(max_attendees: int = 30):
    user_RSVP = 0
    if user_RSVP < max_attendees:
        user_RSVP += 1
    else:
        print("Sorry, event fully booked.")