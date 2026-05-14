from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.api.deps import get_db
from core.domain.models import Alert

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("")
def list_alerts(db: Session = Depends(get_db)):
    return db.query(Alert).order_by(Alert.id.desc()).all()


@router.post("")
def create_alert(payload: dict, db: Session = Depends(get_db)):
    alert = Alert(rule_name=payload.get("rule_name", "unknown"), payload=payload)
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert
