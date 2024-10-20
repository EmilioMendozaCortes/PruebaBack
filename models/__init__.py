from .employees import Employee
from config.db import Base, engine

# Crea todas las tablas
Base.metadata.create_all(bind=engine)
