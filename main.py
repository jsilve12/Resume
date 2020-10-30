"""Origin for FastAPI."""

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from .website import base

app = FastAPI()
app.mount('/static', StaticFiles(directory='Resume/static'), name='static')


app.include_router(
    base.app,
    tags=['webpage']
)
