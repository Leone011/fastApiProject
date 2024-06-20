from contextlib import asynccontextmanager
from fastapi import FastAPI
from tortoise import Tortoise
from app.db.tortoise_config import TORTOISE_ORM
from app.routers import config, business


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    yield
    # Shutdown
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)

app.include_router(config.router, prefix="/api/config", tags=["config"])
app.include_router(business.router, prefix="/api/business", tags=["business"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
