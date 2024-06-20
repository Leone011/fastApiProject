# app/db/tortoise_config.py

TORTOISE_ORM = {
    "connections": {
        "sqlite": "sqlite://db_config.sqlite3",  # SQLite 连接 URL
        "postgresql": "postgres://yanyu:yanyu@2024@linux01:5432/business_db",  # PostgreSQL 连接 URL
    },
    "apps": {
        "config_models": {
            "models": ["app.db.models.config_models"],  # 只包含配置模型
            "default_connection": "sqlite",  # 配置相关模型默认连接为 SQLite
        },
        "business_models": {
            "models": ["app.db.models.business_models"],  # 只包含业务模型
            "default_connection": "postgresql",  # 业务相关模型默认连接为 PostgreSQL
        },
    },
    "use_tz": False,
    "timezone": "UTC"
}
