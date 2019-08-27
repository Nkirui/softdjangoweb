# Dockerfile
# FROM directive instructing base image to build upon
FROM python:3.5
MAINTAINER nathankirui5@gmail.com
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /mdata
WORKDIR /mdata
COPY . /mdata
RUN pip install -r requirements.txt
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# build app
RUN pip install -r requirements.txt
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput 
RUN python manage.py test --noinput

# Run command to create supperuser 
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'nathankirui5@gmail.com', 'adminpass12345')" | python manage.py shell

# Run CMD command to start the server
CMD python manage.py runserver 0.0.0.0:8000
# --insecure


