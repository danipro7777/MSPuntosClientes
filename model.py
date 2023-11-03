from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Double, Integer, Date, Boolean
from database import Base


class Cliente(Base):
    _tablename_ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    telefono = Column(String(100))
    direccion = Column(String(100))
    frecuente = Column(String(100))
    puntosAcumulados = Column(Integer)