from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

# Data schema defined with Pydantic
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=3, example="Laptop Gamer")
    price: float = Field(..., gt=0)
    stock: int = Field(default=10, ge=0)


@router.post("/", status_code=201)
async def create_item(item: ItemCreate):
    # Here Pydantic already validated item properties
    if item.price > 10000:
        raise HTTPException(status_code=400, detail="Price too high")
    
    return {"message": "Item created successfully", "data": item}
