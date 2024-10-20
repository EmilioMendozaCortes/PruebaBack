# Importación de dependencias
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from typing import Optional, List

# Modelo del empleado
class Employee(Base):
    __tablename__ = 'Employees'
    ID = Column(Integer, primary_key=True, index=True)
    Nombres = Column(String(80), nullable=False)
    Primer_Apellido = Column(String(80), nullable=False)
    Segundo_Apellido = Column(String(80), nullable=False)
    CURP = Column(String(18), nullable=False, unique=True)
    Puesto = Column(String(45))
    ClaveEmpleado = Column(String(12), nullable=False)
    Calle = Column(String(40), nullable=False)
    NoExterior = Column(Integer, nullable=False)
    NoInterior = Column(Integer)
    Colonia = Column(String(40), nullable=False)
    Municipio = Column(String(40), nullable=False)
    Estado = Column(String(50), nullable=False)
    Pais = Column(String(47), nullable=False)
    Fecha_Registro = Column(DateTime, nullable=False)
    Fecha_Actualizacion = Column(DateTime)
    # Relaciones
    Clave_Jefe_Inmediato = Column(Integer, ForeignKey('Employees.ID'), nullable=True)
    subordinados = relationship("Employee", backref='jefe', remote_side=[ID])