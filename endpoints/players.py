
from fastapi import APIRouter, status, HTTPException
from models import Playerbase, PlayerDB, PlayerPost, EventDB2, types

router = APIRouter()

players = []   #Tyhjä pelaajalista

@router.post("/players", status_code=201, response_model=PlayerPost)        #Uusien pelaajien luominen
def create_player(player_in: Playerbase):
  global id_counter
  if not players:
     id_counter = 0
  player = PlayerDB(id=id_counter, name=player_in.name)
  players.append(player.model_dump())
  id_counter += 1
  return player

@router.get("/players", response_model=list[PlayerPost],status_code=200)    #Hae kaikki pelaajat
def get_players():
   return players

@router.get('/players/{id}', response_model=PlayerDB)                       #Hae pelaaja ID:n perusteella
def get_player(id: int):
    indexi = -1
    for x, y in enumerate(players):
        if y['id'] == id:
            indexi = x
            break
    if indexi == -1:
        raise HTTPException(detail="Player not found", status_code=404)
    return players[indexi]

@router.get('/players/{id}/events', response_model=list[EventDB2], status_code=201) #Hae pelaaja ID:n perusteella kaikki haetun pelaajan eventit. Mahdollista myös filtteröidä eventit ("level_started" tai "level_solved")
def get_playerevents(id: int, type: str = None):
    player = get_player(id)
    player_events = [dict(event) for event in player['events']]

    if type not in types and not None:
        raise HTTPException(status_code=400, detail="Invalid event type")

    if type:
        events_by_type = [
            event for event in player_events if event ['type'] == type
        ]
        player_events = events_by_type
    return player_events
