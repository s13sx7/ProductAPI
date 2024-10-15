from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    NAME: str

    
    class Config:
        env_file = '.env'

settings = Settings()

def get_url():
    return f"postgresql+asyncpg://{settings.USER}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.NAME}"
