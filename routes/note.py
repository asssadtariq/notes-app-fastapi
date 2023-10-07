from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note as noteModel
from config.db import conn
from fastapi.templating import Jinja2Templates

from schemas.note import noteEntity, notesEntity # noteEntity of one item - notesEntity for a list of item

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_note(request: Request):
    doc = conn.Practice.Practice_DB.find()
    return templates.TemplateResponse("mynotes.html", {"request": request, "data": doc})

@note.get("/create_notes", response_class=HTMLResponse)
async def read_note(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@note.post("/create", response_class=HTMLResponse)
async def create_note(request: Request):
    form = await request.form()
    print(form)
    formDict = dict(form)
    # formDict['isImportant'] = True if formDict['isImportant'] == "on" else False
    if "isImportant" not in formDict.keys():
        formDict["isImportant"] = False
    note = conn.Practice.Practice_DB.insert_one(formDict)

    message = "Failed To Upload New Note"
    if note:
        message = "New Note Uploaded"

    return templates.TemplateResponse("index.html", {"request": request, "message": message})

