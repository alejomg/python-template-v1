# Punto de entrada (instancia FastAPI)

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.endpoints import items
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Lógica de ARRANQUE (Startup) ---
    print(f"starting up {settings.PROJECT_NAME}...")
    # print("Conectando a la base de datos...")
    # Ejemplo: await database.connect()
    
    yield  # Aquí es donde la aplicación "vive" y atiende peticiones
    
    # --- Lógica de CIERRE (Shutdown) ---
    print(f"shutting down {settings.PROJECT_NAME}...")
    # print("Cerrando recursos y limpieza...")
    # Ejemplo: await database.disconnect()

#app = FastAPI(lifespan=lifespan)

app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG
)

#para que los router sean visibles
app.include_router(items.router, prefix="/api/v1/items", tags=["Items"])

@app.get("/")
def root():
    return {"message": "API Online"}
    
@app.get("/config-check")
def check_config():
    return {"app_name": settings.PROJECT_NAME}
