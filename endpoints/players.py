
from fastapi import APIRouter, status, HTTPException
from models import Playerbase, PlayerDB, PlayerPost

router = APIRouter()

players = []

@router.post("/players", status_code=status.HTTP_201_CREATED, response_model=PlayerPost)
def create_player(player_in: Playerbase):
  global id_counter
  if not players:
     id_counter = 0
  player = PlayerDB(id=id_counter, name=player_in.name)
  players.append(player.model_dump())
  id_counter += 1
  return player

@router.get("/players", response_model=list[PlayerPost],status_code=200)
def get_players():
   return players

@router.get('/players/{id}', response_model=PlayerDB)
def get_player(id: int):
    indexi = -1
    for x, y in enumerate(players):
        if y['id'] == id:
            indexi = x
            break
    if indexi == -1:
        raise HTTPException(detail="Player not found", status_code=404)
    return players[indexi]