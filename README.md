# durls
**D**jango **URL** **S**hortener

## Development
1. Using pipenv:
```bash
git clone https://github.com/almazkun/durls.git
cd durls
pipenv install
pipenv shell
python3 manage.py runserver
# Open your browser and navigate to `127.0.0.1:8000` or `localhost`
```

2. To use docker:
```bash
git clone https://github.com/almazkun/durls.git
cd durls
docker build -t durls .
docker run --rm -d -p 80:8000 durls
# Open your browser and navigate to `127.0.0.1` or `localhost`
```

3. To add a new redirect destination:
    - start the server
    - Open your browser and navigate to `127.0.0.1:80/_/`
    - add a new slug and destination URL

### TODO

- Homepage on empty slug
- Slug checker, to remove "/"
- Mount volume for code change
- Production setup

## Deploy

1. https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-github-actions/

2. https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

3. https://testdriven.io/blog/django-lets-encrypt/
