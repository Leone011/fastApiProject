# app/db/models/business_models.py

from tortoise import fields
from tortoise.models import Model


class BusinessRecord(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=2)
    value = fields.FloatField()

    class Meta:
        table = "business_records"
        using_db = "postgresql"  # 明确指定使用 PostgreSQL 连接
