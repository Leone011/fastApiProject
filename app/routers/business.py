# app/routers/business.py

from fastapi import APIRouter, HTTPException
from app.schemas import BusinessCreate, BusinessRead
from app.crud.business_crud import create_record, get_record, update_record, delete_record

router = APIRouter()


@router.post("/", response_model=BusinessRead)
async def create_record_endpoint(record: BusinessCreate):
    db_record = await create_record(record.name, record.value)
    return db_record


@router.get("/{id}", response_model=BusinessRead)
async def get_record_endpoint(id: int):
    record = await get_record(id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return record


@router.put("/{id}", response_model=BusinessRead)
async def update_record_endpoint(id: int, record: BusinessCreate):
    updated_record = await update_record(id, record.name, record.value)
    if updated_record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return updated_record


@router.delete("/{id}", response_model=bool)
async def delete_record_endpoint(id: int):
    return await delete_record(id)
