# syntax=docker/dockerfile:1

# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./dj .

EXPOSE 8080

CMD gunicorn proj.wsgi --bind 0.0.0.0:8080 --workers 4

## Docker Related
# ***************
# CMD ["python", "dj/manage.py", "runserver", "0.0.0.0:8080"]
# docker stop $(docker container ps -a -q)
# docker rm $(docker container ps -a -q)
# docker rmi $(docker images -a -q)
# docker build -t kameri-service . --file deploy.dockerfile
# docker run -p 8080:8080 -it kameri-service
# docker run --env PORT=8000 --env DOWNLOAD_BASE_URL=https://raw.githubusercontent.com/AbrarNitk/abrark/main/ -p 8000:8000 -it fpm-docker:latest
# ***************

## Django service related
# ***************
# gunicorn martor_demo.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
# gunicorn proj.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
