import os
print("=====")
print(os.getcwd())

from fastapi import FastAPI

from api import routes
from db.database import engine, Base
import core.redis as redis_cache
import redis 

app = FastAPI(title="FastAPI App")

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize Redis
@app.on_event("startup")
async def startup_event():
    redis_client = redis_cache.get_redis()
    try:
        # Check if Redis is accessible
        redis_client.ping()
        print("Successfully connected to Redis")
    except redis.exceptions.ConnectionError:
        print("Failed to connect to Redis")

@app.on_event("shutdown")
async def shutdown_event():
    await redis_cache.close_redis()

# Include routes
app.include_router(routes.router)

