#!/usr/bin/env bash
set -e
cd /opt/assistant_copro_10m
echo "[1/3] Git pull..."
git pull --rebase
echo "[2/3] (Optionnel) dépendances API"
# . api/.venv/bin/activate && pip install -r api/requirements.txt
echo "[3/3] Restart PM2..."
pm2 restart assistant_api
pm2 save
echo "OK."
