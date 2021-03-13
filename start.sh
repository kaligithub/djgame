#!/bin/bash

# Makemigration
# echo Starting Makemigration.
# python3 manage.py makemigrations

# Migrate
echo Starting Migration.
python3 manage.py migrate

# Create superuser
echo Creating superuser.
python3 manage.py createcustomsuperuser

# Collect static files
echo Collecting static files.
python3 manage.py collectstatic --no-input

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn play.wsgi:application \
    --bind 0.0.0.0:9000 \
    --workers 3 \
    --log-level=info \
    --timeout 120