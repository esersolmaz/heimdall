from pydantic import BaseModel
import os


class Settings(BaseModel):
    env: str = os.getenv("HEIMDALL_ENV", "dev")
    api_host: str = os.getenv("HEIMDALL_API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("HEIMDALL_API_PORT", "8000"))
    database_url: str = os.getenv("HEIMDALL_DATABASE_URL", "sqlite+pysqlite:///./heimdall.db")
    redis_url: str = os.getenv("HEIMDALL_REDIS_URL", "redis://localhost:6379/0")
    celery_broker_url: str = os.getenv("HEIMDALL_CELERY_BROKER_URL", "redis://localhost:6379/1")
    celery_result_backend: str = os.getenv("HEIMDALL_CELERY_RESULT_BACKEND", "redis://localhost:6379/2")


settings = Settings()
