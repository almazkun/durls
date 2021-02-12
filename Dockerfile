FROM python:buster

WORKDIR /usr/src/code

EXPOSE 80

RUN apt-get update && apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

run pip3 install pipenv

COPY Pipfile ./

run pipenv lock

RUN pipenv install --system

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]