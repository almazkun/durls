FROM python:buster

WORKDIR /usr/src/code

RUN apt-get update && apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

RUN pip3 install pipenv

COPY ./Pipfile .

COPY ./Pipfile.lock .

RUN pipenv install --deploy --system --ignore-pipfile

COPY . .

RUN useradd -m ubuntu -s /bin/bash -p heW0jFpcTWOG2

RUN usermod -a -G sudo ubuntu

USER ubuntu