# Importación de dependencias
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from typing import List
import random
from datetime import datetime
import models.employees as models
import schemas.employees as schemas

# Listar los empleados con sus subordinados
def get_employees(db: Session, skip: int = 0, limit: int = 1):
    employees = db.query(models.Employee).offset(skip).limit(limit).all()
    employee_responses = []
    for employee in employees:
        employee_responses.append(schemas.Employee(
            ID=employee.ID,
            Nombres=employee.Nombres,
            Primer_Apellido=employee.Primer_Apellido,
            Segundo_Apellido=employee.Segundo_Apellido,
            CURP=employee.CURP if employee.CURP else "N/A",
            Puesto=employee.Puesto,
            Calle=employee.Calle if employee.Calle else "Sin Calle",
            NoExterior=employee.NoExterior if employee.NoExterior else 0,
            NoInterior=employee.NoInterior,
            Colonia=employee.Colonia if employee.Colonia else "Sin Colonia",
            Municipio=employee.Municipio if employee.Municipio else "Sin Municipio",
            Estado=employee.Estado if employee.Estado else "Sin Estado",
            Pais=employee.Pais if employee.Pais else "Sin País",
            Clave_Jefe_Inmediato=employee.Clave_Jefe_Inmediato if employee.Pais else "No tiene",
            # Llama a get_subordinates para cada empleado
            subordinados=get_subordinates(db, employee.ID)  
        ))
    return employee_responses

# Obtener los subordinados de un empleado específico
def get_subordinates(db: Session, employee_id: int) -> List[schemas.Employee]:
    subordinates = db.query(models.Employee).filter(models.Employee.Clave_Jefe_Inmediato == employee_id).all()
    subordinate_responses = []
    for subordinate in subordinates:
        if not (subordinate.CURP and subordinate.Calle and subordinate.NoExterior and 
                subordinate.Colonia and subordinate.Municipio and subordinate.Estado and subordinate.Pais):
            continue 
        subordinate_responses.append(schemas.Employee(
            ID=subordinate.ID,
            Nombres=subordinate.Nombres,
            Primer_Apellido=subordinate.Primer_Apellido,
            Segundo_Apellido=subordinate.Segundo_Apellido,
            CURP=subordinate.CURP,
            Puesto=subordinate.Puesto,
            Calle=subordinate.Calle,
            NoExterior=subordinate.NoExterior,
            NoInterior=subordinate.NoInterior,
            Colonia=subordinate.Colonia,
            Municipio=subordinate.Municipio,
            Estado=subordinate.Estado,
            Pais=subordinate.Pais,
            Clave_Jefe_Inmediato=subordinate.Clave_Jefe_Inmediato if subordinate.Clave_Jefe_Inmediato is not None else None,
            # Lamada recursiva de los subordinados
            subordinados=get_subordinates(db, subordinate.ID)  
        ))
    return subordinate_responses

# Generar número
def generate_number_random(curp: str):
    base_clave = curp[:10]
    num_random = str(random.randint(10, 99))
    return f"{base_clave}{num_random}"

# Crear un nuevo empleado
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    clave_empleado_generada = generate_number_random(employee.CURP)
    db_employee = models.Employee(
        Nombres=employee.Nombres,
        Primer_Apellido=employee.Primer_Apellido,
        Segundo_Apellido=employee.Segundo_Apellido,
        CURP=employee.CURP,
        Puesto=employee.Puesto,
        ClaveEmpleado=clave_empleado_generada,
        Calle=employee.Calle,
        NoExterior=employee.NoExterior,
        NoInterior=employee.NoInterior,
        Colonia=employee.Colonia,
        Municipio=employee.Municipio,
        Estado=employee.Estado,
        Pais=employee.Pais,
        Fecha_Registro=datetime.utcnow(),
        Fecha_Actualizacion=None,
        Clave_Jefe_Inmediato=employee.Clave_Jefe_Inmediato
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Actualizar un empleado por ID
def update_employee(db: Session, id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.ID == id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    for var, value in employee.dict(exclude_unset=True).items():
        setattr(db_employee, var, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee