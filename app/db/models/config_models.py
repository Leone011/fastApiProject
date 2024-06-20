# app/db/models/config_models.py

from tortoise import fields
from tortoise.models import Model


class SystemConfig(Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=50, unique=True)
    value = fields.TextField()

    class Meta:
        table = "system_configs"
        using_db = "sqlite"  # 明确指定使用 SQLite 连接
