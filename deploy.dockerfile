# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8080

# gunicorn martor_demo.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3

# gunicorn proj.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3

WORKDIR /code/dj

CMD ["gunicorn", "proj.wsgi", "--bind", "0.0.0.0:8080", "--workers", "4"]

# CMD ["python", "dj/manage.py", "runserver", "0.0.0.0:8080"]

# docker stop $(docker container ps -a -q)
# docker rm $(docker container ps -a -q)
# docker rmi $(docker images -a -q)
# docker build -t kameri-service . --file deploy.dockerfile
# docker run -p 8080:8080 -it kameri-service


# docker run --env PORT=8000 --env DOWNLOAD_BASE_URL=https://raw.githubusercontent.com/AbrarNitk/abrark/main/ -p 8000:8000 -it fpm-docker:latest
