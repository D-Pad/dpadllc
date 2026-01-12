#!/bin/bash 


mkdir -p "$LOG_PATH"


gunicorn -w 2 \
    --bind 0.0.0.0:$WEBPAGE_API_PORT \
    --timeout 600 \
    app_server.wsgi:app \
    --access-logfile - \
    --error-logfile -

