from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note as routeNote

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name='static')

app.include_router(routeNote)

