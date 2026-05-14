from sqlalchemy.orm import Session

from core.domain.enums import PlaybookRunStatus, PlaybookStepStatus
from core.domain.models import PlaybookRun, PlaybookStep


class PlaybookStateMachine:
    allowed_run_transitions = {
        PlaybookRunStatus.PENDING: {PlaybookRunStatus.RUNNING, PlaybookRunStatus.FAILED},
        PlaybookRunStatus.RUNNING: {PlaybookRunStatus.WAITING_APPROVAL, PlaybookRunStatus.SUCCESS, PlaybookRunStatus.FAILED},
        PlaybookRunStatus.WAITING_APPROVAL: {PlaybookRunStatus.RUNNING, PlaybookRunStatus.FAILED},
        PlaybookRunStatus.SUCCESS: set(),
        PlaybookRunStatus.FAILED: set(),
    }

    @classmethod
    def transition_run(cls, run: PlaybookRun, new_status: PlaybookRunStatus) -> None:
        current = PlaybookRunStatus(run.status)
        if new_status not in cls.allowed_run_transitions[current]:
            raise ValueError(f"Invalid playbook run transition: {current} -> {new_status}")
        run.status = new_status.value



def create_run_with_steps(db: Session, playbook_name: str, payload: dict) -> PlaybookRun:
    run = PlaybookRun(playbook_name=playbook_name, status=PlaybookRunStatus.PENDING.value)
    db.add(run)
    db.flush()

    step = PlaybookStep(
        run_id=run.id,
        step_id="notify",
        action="notify",
        status=PlaybookStepStatus.PENDING.value,
        input_payload=payload,
    )
    db.add(step)
    db.commit()
    db.refresh(run)
    return run
