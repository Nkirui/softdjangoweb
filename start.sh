#!/bin/bash

python manage.py migrate --noinput     # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

python manage.py runserver 0.0.0.0:8000


Start Gunicorn processes
echo Now starting Gunicorn.
exec gunicorn softsearchcbs.wsgi:application --bind 0.0.0.0:8000 --workers 3
