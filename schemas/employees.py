# Importación de dependencias
from typing import List, Optional
from pydantic import BaseModel

# Esquema del modelo del empleado
class EmployeeBase(BaseModel):
    Nombres: str
    Primer_Apellido: str
    Segundo_Apellido: str
    CURP: str
    Puesto: Optional[str] = None
    Calle: str
    NoExterior: int
    NoInterior: Optional[int] = None
    Colonia: str
    Municipio: str
    Estado: str
    Pais: str
    Clave_Jefe_Inmediato: Optional[int] = None
    subordinados: List[Optional['Employee']] = []

# Metodo para crear un emlpeado con sus parametros
class EmployeeCreate(EmployeeBase):
    pass

# Metodo para actualizar un empleado con sus parametros
class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    ID: int
    class Config:
        orm_mode = True