from fastapi import FastAPI
from typing import List
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import model, schemas
from database import SessionLocal,engine
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def  main():
    return RedirectResponse(url="/docs/")

@app.get('/clientes/',response_model=List[schemas.Cliente])
def show_users(db:Session=Depends(get_db)):
    clientes = db.query(model.User).all()
    return clientes

@app.post('/clientes/',response_model=schemas.Cliente)
def create_users(entrada:schemas.Cliente,db:Session=Depends(get_db)):
    clientes = model.nombre(nombre = entrada.nombre,telefono=entrada.telefono,direccion=entrada.direccion,frecuente=entrada.frecuente,puntosAcumulados=entrada.puntosAcumulados)
    db.add(clientes)
    db.commit()
    db.refresh(clientes)
    return clientes

@app.put('/clientes/{usuario_id}',response_model=schemas.Cliente)
def update_users(usuario_id:int,entrada:schemas.ClienteUpdate,db:Session=Depends(get_db)):
    clientes = db.query(model.User).filter_by(id=usuario_id).first()
    clientes.nombre=entrada.nombre
    db.commit()
    db.refresh(clientes)
    return clientes

@app.delete('/clientes/{usuario_id}',response_model=schemas.Respuesta)
def delete_users(usuario_id:int,db:Session=Depends(get_db)):
    clientes = db.query(model.User).filter_by(id=usuario_id).first()
    db.delete(clientes)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta