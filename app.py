# Importación de dependencias
from fastapi import FastAPI
from routes.employees import employee_router 

app = FastAPI()

# Ejecución de la aplicación
app.include_router(employee_router)
print("Prueba técnica de backend")
