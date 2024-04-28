from fastapi import FastAPI, HTTPException, status
from endpoints import players,events

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)
