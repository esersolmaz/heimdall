from celery import Celery
from core.config import settings

celery_app = Celery(
    "heimdall-worker",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)
celery_app.autodiscover_tasks(["apps.worker.tasks"])
