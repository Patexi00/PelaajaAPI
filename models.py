from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    type: str
    details: str
    timestamp: str

class EventInSpec(BaseModel):
    type: str
    details: str

class EventDB(EventInSpec):
    player_id: int

class EventDB2(Event):
    player_id: int

class Playerbase(BaseModel):
    name: str

class PlayerPost(BaseModel):
    name: str
    id: int

class PlayerDB(PlayerPost):
   events: List[EventDB2] = []