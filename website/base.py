""" Core Website Pages """
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


app = APIRouter()
templates = Jinja2Templates(directory='Resume/templates')


@app.get('/', response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
