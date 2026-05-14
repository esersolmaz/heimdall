from fastapi import APIRouter
from apps.worker.tasks.playbook_tasks import run_playbook

router = APIRouter(prefix="/playbooks", tags=["playbooks"])


@router.post("/{playbook_name}/run")
def trigger_playbook(playbook_name: str, payload: dict):
    task = run_playbook.delay(playbook_name, payload)
    return {"task_id": task.id, "status": "queued"}
