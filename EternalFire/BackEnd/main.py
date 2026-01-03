from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from models.genero import Genero

import uvicorn


app = FastAPI(title="Eternal Fire API", version="1.0.0")
db_generos = []

@app.get("/")
async def root():
    return {"message": "Welcome to the Eternal Fire API"}


@app.get("/generos", response_model=List[Genero])
async def get_Allgeneros():
    return db_generos


@app.get("/generos/{nombre}", response_model=Genero)
async def get_genero_by_name(nombre: str):
    genero = next((g for g in db_generos if g.nombre.lower() == nombre.lower()), None)
    if genero is None:
        raise HTTPException(status_code=404, detail="El genero: " + nombre + " no ha sido encontrado")
    return genero



@app.post("/generos", status_code=201, response_model=Genero)
async def create_genero(genero: Genero):
    new_id = db_generos[-1].id + 1 if db_generos else 1
    genero.id = new_id
    db_generos.append(genero)
    return genero


@app.put("/generos/{id}", response_model=Genero, status_code=200)
async def update_genero(id :int, updated_genero: Genero):
    generoID = next((g for g in db_generos if g.id == id), None)
    if generoID is None:
        raise HTTPException(status_code=404, detail="El genero con id: " + str(id) + " no ha sido encontrado")
    else:
        generoID.nombre = updated_genero.nombre
        generoID.historia = updated_genero.historia
        generoID.filosofia = updated_genero.filosofia
        generoID.artistas_destacados = updated_genero.artistas_destacados
        generoID.subgeneros = updated_genero.subgeneros
        return generoID
    



@app.delete("/generos/{id}", status_code=204)
async def delete_genero(id : int):
    generoID = next((g for g in db_generos if g.id == id), None)
    if generoID is None:
        raise HTTPException(status_code=404, detail="El genero con id: " + str(id) + " no ha sido encontrado")
    db_generos.remove(generoID)
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
