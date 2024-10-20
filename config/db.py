# Importación de dependencias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión local a Workbench
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://tuUsuario:tuContraseña@localhost:tuPuerto/employees'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
