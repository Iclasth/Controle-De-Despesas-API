from fastapi import FastAPI

app=FastAPI()

from roteador import roteador
from autenticador import autenticador


app.include_router(autenticador)
app.include_router(roteador)