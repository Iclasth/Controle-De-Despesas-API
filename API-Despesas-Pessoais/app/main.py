from fastapi import FastAPI

app = FastAPI(title="API de Controle de Despesas Pessoais - Iclas")

@app.get("/")
def root():
    return {"status": "ok"}
