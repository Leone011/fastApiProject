# app/crud/business_crud.py

from app.db.models.business_models import BusinessRecord


async def create_record(name: str, value: float):
    return await BusinessRecord.create(name=name, value=value)


async def get_record(id: int):
    return await BusinessRecord.get_or_none(id=id)


async def update_record(id: int, name: str, value: float):
    record = await get_record(id)
    if record:
        record.name = name
        record.value = value
        await record.save()
        return record
    return None


async def delete_record(id: int):
    record = await get_record(id)
    if record:
        await record.delete()
        return True
    return False
