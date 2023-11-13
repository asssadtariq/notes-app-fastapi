from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routes.note import note as routeNote
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name='static')
templates = Jinja2Templates(directory="templates")
app.include_router(routeNote)

@app.get("/{path:path}", response_class=HTMLResponse)
async def catch_all(request: Request):
    error_message = "Page Not Found"
    return templates.TemplateResponse("error.html", {'request': request, "error": error_message, "status_code": 404})
