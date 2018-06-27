#!/usr/bin/env bash
flask db upgrade
exec /opt/conda/envs/app/bin/uwsgi --ini /app/scripts/uwsgi.ini