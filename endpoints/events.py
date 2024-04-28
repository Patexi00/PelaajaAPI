from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from endpoints.players import get_player
from models import EventInSpec, EventDB2, types, events


router = APIRouter()



@router.post('/players/{id}/events', status_code=201, response_model=EventDB2)      #Luo uusi eventti pelaajalle ID:n perusteella
def create_events(id: int, event_in: EventInSpec):
    global event_counter
    player = get_player(id)
    if not events:
     event_counter = 0

    if event_in.type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    event = EventDB2(
        id=event_counter, type=event_in.type, details=event_in.details,
        timestamp=datetime.now().strftime('%Y-%m-%d, %H:%M:%S'),player_id=id
    )
    events.append(event.model_dump())
    player['events'].append(event)
    event_counter +=1

    return event

@router.get('/events', response_model=list[EventDB2],status_code=200)               #Hae kaikki kirjatut eventit, mahdollista suorittaa filtteröinti event-tyypin mukaan. ("level_started" tai "level_solved")
def get_all_events(type: str = None):
   if type is not None and type not in types:
      raise HTTPException(status_code=400, detail="Invalid event type")
   
   if type is not None:
      all_events_by_type = [
      event for event in events if event['type'] == type
      ]
      return all_events_by_type
   if type is None:
       return events
  