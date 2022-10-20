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

# add and run as non-root user
# RUN useradd -D www-data
# USER www-data


RUN pip install -r requirements.txt

# copy project
COPY ./dj .

EXPOSE 8080

# run gunicorn, commented out for
CMD gunicorn proj.wsgi:application --bind 0.0.0.0:$PORT --workers 4

# CMD python manage.py runserver 0.0.0.0:8080

## Docker Related
# ***************
# CMD ["python", "dj/manage.py", "runserver", "0.0.0.0:8080"]
# docker stop $(docker container ps -a -q)
# docker rm $(docker container ps -a -q)
# docker rmi $(docker images -a -q)
# docker build -t kameri-service . --file deploy.dockerfile
# docker run -p 8080:8080 -e "PORT=8080" -it kameri-service

# docker run --env PORT=8000 --env DOWNLOAD_BASE_URL=https://raw.githubusercontent.com/AbrarNitk/abrark/main/ -p 8000:8000 -it fpm-docker:latest

# ***************

# ***************
## Django service related
# ***************
# gunicorn martor_demo.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
# gunicorn proj.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3

# ***************
## Heroku Setup
# ***************

# Create an app
# heroku apps:create kameri-service --manifest
# app name: kameri-service

# Deploy an app
# heroku stack:set container -a kameri-service
# heroku git:remote -a kameri-service
# Deploy the application
# git push heroku main

# Destroy an app
# heroku apps:destroy kameri-service

# heroku check file system
# heroku run ls /app -a kameri-service

# Create a heroku database
# heroku addons:create heroku-postgresql:hobby-dev -a kameri-service
# This command will automatically setup the DATABASE_URL

# Once the database is up, run the migrations
# heroku run python manage.py makemigrations -a kameri-service
# heroku run python manage.py migrate -a kameri-service

# Article
# https://devcenter.heroku.com/articles/build-docker-images-heroku-yml