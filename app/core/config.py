from pydantic_settings import BaseSettings
from typing import Optional

from dotenv import load_dotenv
import os

load_dotenv()  # This loads environment variables from the .env file
print(os.getenv('POSTGRES_PORT'))  # This should print 5432

class Settings(BaseSettings):
    # Database settings
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    
    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: int
    
    class Config:
        env_file = ".env"

settings = Settings() 