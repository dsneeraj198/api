# routers/sum_router.py

from fastapi import APIRouter, HTTPException
from typing import Dict
from app.utils.transform import fn_transforminput
from app.schemas.transform import Input
router = APIRouter()

@router.post("/lower", response_model=Dict[str, str])
async def calculate_sum(inputinfo: Input) -> Dict[str, str]:
    data = inputinfo.input2
    result = fn_transforminput(data)
    return {"lower": result}
