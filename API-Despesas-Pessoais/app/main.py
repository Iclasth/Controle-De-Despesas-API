from fastapi import FastAPI
from app.db import Base, engine
from app import models
from app.routers import expenses

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Controle de Despesas Pessoais - Iclas")

app.include_router(expenses.router)