from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import players,events

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)

app.add_middleware(             #Sallitaan pääsy sisään kaikista lähteistä
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)