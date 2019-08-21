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

# CMD specifcies the command to execute to start the server running.

CMD ["python", "./manage.py","migrate","runserver", "0.0.0.0:8000"]
CMD ["./start.sh"]


