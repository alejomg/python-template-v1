from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

# Definimos el esquema de datos con Pydantic
class ItemCreate(BaseModel):
    nombre: str = Field(..., min_length=3, example="Laptop Gamer")
    precio: float = Field(..., gt=0)
    stock: int = Field(default=10, ge=0)

@router.post("/crear", status_code=201)
async def create_item(item: ItemCreate):
    # Aquí Pydantic ya validó que 'nombre' sea string, 
    # 'precio' sea número positivo, etc.
    if item.precio > 10000:
        raise HTTPException(status_code=400, detail="Precio demasiado alto")
    
    return {"mensaje": "Producto creado con éxito", "data": item}
