# routers/sum_router.py

from fastapi import APIRouter, HTTPException
from typing import Dict
from app.utils.compute import add_numbers
from app.schemas.sum_router import Numbers
router = APIRouter()

@router.post("/sum", response_model=Dict[str, float])
async def calculate_sum(numbers: Numbers) -> Dict[str, float]:
    num1 = numbers.num1
    num2 = numbers.num2
    result = add_numbers(num1,num2)
    return {"sum": result}
