# app/crud/config_crud.py

from app.db.models.config_models import SystemConfig


async def create_config(key: str, value: str):
    return await SystemConfig.create(key=key, value=value)


async def get_config(key: str):
    return await SystemConfig.get_or_none(key=key)


async def update_config(key: str, value: str):
    config = await get_config(key)
    if config:
        config.value = value
        await config.save()
        return config
    return None


async def delete_config(key: str):
    config = await get_config(key)
    if config:
        await config.delete()
        return True
    return False
