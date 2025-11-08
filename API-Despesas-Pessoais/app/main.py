from fastapi import FastAPI
from app.db import Base, engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Controle de Despesas Pessoais - Iclas")

@app.get("/")
def root():
    return {"status": "ok"}
