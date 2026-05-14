from fastapi import FastAPI

from apps.api.routers import auth, alerts, incidents, cases, playbooks, connectors
from infra.db.base import Base
from infra.db.session import engine

app = FastAPI(title="Heimdall SOAR API", version="0.1.0")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(alerts.router)
app.include_router(incidents.router)
app.include_router(cases.router)
app.include_router(playbooks.router)
app.include_router(connectors.router)


@app.get("/health")
def healthcheck():
    return {"status": "ok"}
