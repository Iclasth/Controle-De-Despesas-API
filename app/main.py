from fastapi import FastAPI

# Importações corretas
from app.core.db import engine, Base  # Base e engine do core/db
from app.controllers.routers import expenses  # rotas

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Instância do FastAPI
app = FastAPI(title="API de Controle de Despesas Pessoais - Iclas")

# Registro das rotas
app.include_router(expenses.router)
