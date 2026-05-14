from apps.worker.celery_app import celery_app
from core.domain.enums import PlaybookRunStatus, PlaybookStepStatus
from core.domain.models import PlaybookRun
from core.services.playbook_service import PlaybookStateMachine
from infra.db.session import SessionLocal


@celery_app.task(bind=True, max_retries=3)
def run_playbook(self, run_id: int):
    db = SessionLocal()
    try:
        run = db.get(PlaybookRun, run_id)
        if not run:
            return {"ok": False, "error": "run_not_found"}

        PlaybookStateMachine.transition_run(run, PlaybookRunStatus.RUNNING)
        for step in run.steps:
            step.status = PlaybookStepStatus.RUNNING.value
            step.output_payload = {"result": "notified"}
            step.status = PlaybookStepStatus.SUCCESS.value

        PlaybookStateMachine.transition_run(run, PlaybookRunStatus.SUCCESS)
        db.commit()
        return {"ok": True, "run_id": run_id, "status": run.status}
    except Exception as exc:
        if 'run' in locals() and run is not None:
            run.status = PlaybookRunStatus.FAILED.value
            db.commit()
        return {"ok": False, "error": str(exc)}
    finally:
        db.close()
