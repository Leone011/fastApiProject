# app/schemas.py

from pydantic import BaseModel


class ConfigCreate(BaseModel):
    key: str
    value: str


class ConfigRead(ConfigCreate):
    id: int

    class Config:
        from_attributes = True


class BusinessCreate(BaseModel):
    name: str
    value: float


class BusinessRead(BusinessCreate):
    id: int

    class Config:
        from_attributes = True
