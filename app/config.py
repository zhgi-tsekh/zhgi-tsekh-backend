import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://zhgi_user:zhgi_password@postgres:5432/zhgi_db"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey123")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
