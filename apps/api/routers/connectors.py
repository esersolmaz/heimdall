from fastapi import APIRouter, HTTPException
from connectors.base.registry import get_connector

router = APIRouter(prefix="/connectors", tags=["connectors"])


@router.post("/{name}/test")
def test_connector(name: str):
    connector = get_connector(name)
    if connector is None:
        raise HTTPException(status_code=404, detail="Connector not found")
    return connector.test_connection()
