from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CELERY_RESULT_BACKEND: str = Field(env="CELERY_RESULT_BACKEND")
    CELERY_RESULT_EXPIRES: str = Field(env="CELERY_RESULT_EXPIRES", default=3600)
    CELERY_BROKER_URL: str = Field(env="CELERY_BROKER_URL")


settings = Settings()
