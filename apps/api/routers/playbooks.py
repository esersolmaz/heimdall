from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.api.deps import get_db
from apps.worker.tasks.playbook_tasks import run_playbook
from core.services.playbook_service import create_run_with_steps

router = APIRouter(prefix="/playbooks", tags=["playbooks"])


@router.post("/{playbook_name}/run")
def trigger_playbook(playbook_name: str, payload: dict, db: Session = Depends(get_db)):
    run = create_run_with_steps(db, playbook_name, payload)
    task = run_playbook.delay(run.id)
    return {"task_id": task.id, "run_id": run.id, "status": "queued"}
