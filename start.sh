#!/bin/bash

# Start Gunicorn processes
echo Now starting Gunicorn.
exec gunicorn softsearchcbs.wsgi:application --bind 0.0.0.0:8000 --workers 3
