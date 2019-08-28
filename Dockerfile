# Dockerfile
# FROM directive instructing base image to build upon
# FROM python:3.5
FROM python:3.7-alpine
MAINTAINER nathankirui5@gmail.com
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /mdata
WORKDIR /mdata
COPY . /mdata

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install Pillow
RUN pip install -r requirements.txt
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# build app
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
# RUN python manage.py collectstatic --noinput 
RUN python manage.py test --noinput

# Run command to create supperuser 
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'nathankirui5@gmail.com', 'adminpass12345')" | python manage.py shell

# Run CMD command to start the server
CMD python manage.py runserver 0.0.0.0:8000  #--insecure


