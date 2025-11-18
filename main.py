from fastapi import FastAPI
from despesas import despesa_router  # importa o roteador do outro arquivo

app = FastAPI(
    title="Controlador de Despesas"
)  # cria a aplicação FastAPI

# inclui o roteador de despesas
app.include_router(despesa_router)


# http://127.0.0.1:8000/docs#/