from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import os
import logging
import traceback
from . import models, database
from .config import settings

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Crear las tablas
models.Base.metadata.create_all(bind=database.engine)

@app.get("/demo/api/country", response_model=models.ApiResponse)
async def get_countries(db: Session = Depends(database.get_db)):
    try:
        # Obtener variables de entorno
        env_vars = [
            models.EnvironmentVar(key=key, value=value)
            for key, value in os.environ.items()
        ]
        
        # Obtener secrets
        secrets = []
        secrets_path = "/etc/secrets"
        if os.path.exists(secrets_path):
            for secret_file in os.listdir(secrets_path):
                with open(os.path.join(secrets_path, secret_file), encoding='utf-8') as f:
                    secrets.append(models.EnvironmentVar(
                        key=secret_file,
                        value=f.read().strip()
                    ))
        
        # Obtener países de la base de datos
        countries = [
            models.Country(code=country.code, name=country.name)
            for country in db.query(models.CountryDB).all()
        ]
        
        return models.ApiResponse(
            environment=env_vars,
            secrets=secrets,
            contries=countries
        )
    except Exception as e:
        logger.error("Error al obtener datos: %s", str(e))
        logger.error("Stack trace: %s", traceback.format_exc())
        raise HTTPException(
            status_code=500, 
            detail="Error interno del servidor: %s" % str(e)
        ) from e

@app.get("/health/liveness")
async def liveness():
    return {"status": "alive"}

@app.get("/health/readiness")
async def readiness(db: Session = Depends(database.get_db)):
    try:
        # Verificar conexión a la base de datos
        db.execute(text("SELECT 1"))
        logger.debug("Readiness check exitoso")
        return {"status": "ready"}
    except Exception as e:
        logger.error("Error en readiness check: %s", str(e))
        logger.error("Stack trace: %s", traceback.format_exc())
        raise HTTPException(
            status_code=503, 
            detail="Service not ready: %s" % str(e)
        ) from e