from fastapi import APIRouter

roteador = APIRouter(prefix='/buscar', tags=['MINHA API'])


@roteador.get('/')
async def buscar():
    return {'voce buscou'}