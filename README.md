# Kameri Service

This repository contains Kameri service. This service written in Django.

# How To Run This Service
- Install python and `git cli` then follow the below steps using terminal
```shell
$ git clone git@github.com:FifthTry/kameri-service.git
$ cd kameri-service
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ python dj/manage.py migrate
$ python dj/manage.py runserver 8001
```

To test it, checkout the [kameri-app], and run it on post 8001.
