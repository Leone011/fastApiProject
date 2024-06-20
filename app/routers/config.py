# app/routers/config.py

from fastapi import APIRouter, HTTPException
from app.schemas import ConfigCreate, ConfigRead
from app.crud.config_crud import create_config, get_config, update_config, delete_config

router = APIRouter()


@router.post("/", response_model=ConfigRead)
async def create_config_endpoint(config: ConfigCreate):
    db_config = await create_config(config.key, config.value)
    return db_config


@router.get("/{key}", response_model=ConfigRead)
async def get_config_endpoint(key: str):
    config = await get_config(key)
    if config is None:
        raise HTTPException(status_code=404, detail="Config not found")
    return config


@router.put("/{key}", response_model=ConfigRead)
async def update_config_endpoint(key: str, config: ConfigCreate):
    updated_config = await update_config(key, config.value)
    if updated_config is None:
        raise HTTPException(status_code=404, detail="Config not found")
    return updated_config


@router.delete("/{key}", response_model=bool)
async def delete_config_endpoint(key: str):
    return await delete_config(key)
