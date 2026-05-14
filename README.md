# Heimdall

Python + FastAPI tabanlı SOAR MVP iskeleti.

## Bileşenler
- API: `apps/api`
- Worker: `apps/worker`
- Scheduler: `apps/scheduler`
- Core domain/services: `core`
- Connector framework: `connectors`
- Infra: `infra`
- Migration: `alembic`

## JWT Auth
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me` (Bearer token gerekli)

## Migration
```bash
alembic upgrade head
```

## Çalıştırma
```bash
docker compose up --build
```
