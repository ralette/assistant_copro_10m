# Assistant Copro 10M

- Page publique: https://assistant.10millionsdecoproprietaires.org
- API santé:   https://assistant.10millionsdecoproprietaires.org/api/health

## Démarrage API (local VPS)
cd /opt/assistant_copro_10m/api
. .venv/bin/activate
uvicorn app.main:app --host 127.0.0.1 --port 8010 --proxy-headers
