# Importación de dependencias
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import config.db
from schemas.employees import Employee, EmployeeCreate, EmployeeUpdate
import crud

employee_router = APIRouter()

# Crear las tablas en la base de datos si no existen
models.Base.metadata.create_all(bind=config.db.engine)
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para listar los empleados
@employee_router.get('/employees/', response_model=List[Employee], tags=['Empleados'])
def read_employees(skip: int = 0, limit: int = 1, db: Session = Depends(get_db)):
    employees = crud.get_employees(db=db, skip=skip, limit=limit)
    return employees

# Ruta para insertar un empleado
@employee_router.post('/employees/', response_model=Employee, tags=['Empleados'])
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = crud.create_employee(db=db, employee=employee)
    return Employee(
        ID=new_employee.ID,
        Nombres=new_employee.Nombres,
        Primer_Apellido=new_employee.Primer_Apellido,
        Segundo_Apellido=new_employee.Segundo_Apellido,
        CURP=new_employee.CURP,
        Puesto=new_employee.Puesto,
        Calle=new_employee.Calle,
        NoExterior=new_employee.NoExterior,
        NoInterior=new_employee.NoInterior,
        Colonia=new_employee.Colonia,
        Municipio=new_employee.Municipio,
        Estado=new_employee.Estado,
        Pais=new_employee.Pais,
        Fecha_Registro=new_employee.Fecha_Registro,
        Fecha_Actualizacion=new_employee.Fecha_Actualizacion,
        subordinados=[]
    )

# Ruta para actualizar un empleado
@employee_router.put('/employees/{id}', response_model=Employee, tags=['Empleados'])
def update_employee(id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    updated_employee = crud.update_employee(db=db, id=id, employee=employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado, no se pudo actualizar")
    return Employee.from_orm(updated_employee)
