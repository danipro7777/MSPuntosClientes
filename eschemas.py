from pydantic import BaseModel

class Cliente(BaseModel):
    id:int
    nombre:str
    telefono:str
    direccion:str
    frecuente:str
    puntosAcumulados:int
    
    class Config:
        orm_mode=True

class ClienteUpdate(BaseModel):   
    nombre:str
   

    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str