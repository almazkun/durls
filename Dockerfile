FROM python:buster

WORKDIR /usr/src/code

RUN adduser --system --group --shell /bin/sh ubuntu \
 && mkdir /home/ubuntu/bin

USER ubuntu

RUN apt-get update && apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

RUN pip3 install pipenv

COPY ./Pipfile .

COPY ./Pipfile.lock .

RUN pipenv install --deploy --system --ignore-pipfile

COPY . .