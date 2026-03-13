from pydantic import BaseSettings

class Settings(BaseSettings):

    DATABASE_URL: str
    REDIS_URL: str
    JWT_SECRET: str

    HUGGINGFACE_API_KEY: str

    YOUTUBE_API_KEY: str
    FACEBOOK_API_KEY: str
    INSTAGRAM_API_KEY: str
    TIKTOK_API_KEY: str

    STRIPE_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
