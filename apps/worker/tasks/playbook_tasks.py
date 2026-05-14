from apps.worker.celery_app import celery_app


@celery_app.task(bind=True, max_retries=3)
def run_playbook(self, playbook_name: str, payload: dict):
    return {
        "playbook": playbook_name,
        "status": "completed",
        "steps": [
            {"id": "notify", "status": "success", "payload": payload}
        ],
    }
