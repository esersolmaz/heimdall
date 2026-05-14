from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.api.deps import get_db
from core.domain.models import Incident

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.get("")
def list_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).order_by(Incident.id.desc()).all()


@router.patch("/{incident_id}")
def update_incident(incident_id: int, payload: dict, db: Session = Depends(get_db)):
    incident = db.get(Incident, incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    for key in ["title", "severity", "status"]:
        if key in payload:
            setattr(incident, key, payload[key])
    db.commit()
    db.refresh(incident)
    return incident
