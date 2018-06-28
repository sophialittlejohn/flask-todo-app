#!/usr/bin/env bash
/opt/conda/envs/app/bin/flask db upgrade
exec /opt/conda/envs/app/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app
