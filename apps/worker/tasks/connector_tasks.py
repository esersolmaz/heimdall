from apps.worker.celery_app import celery_app
from connectors.base.registry import get_connector


@celery_app.task(bind=True, max_retries=3)
def execute_connector_action(self, connector_name: str, action: str, payload: dict):
    connector = get_connector(connector_name)
    if connector is None:
        return {"ok": False, "error": "connector_not_found"}
    return connector.execute_action(action, payload)
