# Dockerfile
# FROM directive instructing base image to build upon
# FROM python:3.5
FROM alpine:3.7
MAINTAINER nathankirui5@gmail.com
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk add --no-cache python3 libffi-dev libxml2-dev libxslt-dev jpeg jpeg-dev libpq supervisor \
 && apk add --no-cache gcc python3-dev musl-dev \
 && python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip \
 && apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev \
 && pip3 install --upgrade pip setuptools \
 && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip; fi \
 && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

RUN mkdir /mdata
WORKDIR /mdata
COPY . /mdata

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
CMD python manage.py runserver 0.0.0.0:8000 --insecure


