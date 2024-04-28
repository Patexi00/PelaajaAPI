from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from endpoints.players import get_player
from models import EventInSpec, EventDB2, Event
from re import match

router = APIRouter()

events = []

types = ['level_started', 'level_solved']

@router.post('/players/{id}/events', status_code=status.HTTP_201_CREATED, response_model=EventDB2)
def create_events(id: int, event_in: EventInSpec):
    player = get_player(id)
    eventcounter = 0

    if event_in.type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    event = EventDB2(
        id=eventcounter, type=event_in.type, details=event_in.details,
        timestamp=datetime.now().strftime('%Y-%m-%d, %H:%M:%S'),player_id=id
    )
    events.append(event.model_dump())
    player['events'].append(event)
    eventcounter +=1

    return event
