# durls
**D**jango **URL** **S**hortener

## Demo at:
https://durls.akun.dev/

## Start Server
1. Using pipenv:
```bash
git clone https://github.com/almazkun/durls.git
cd durls
pipenv install
pipenv shell
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 127.0.0.1:80
# Open your browser and navigate to `127.0.0.1` or `localhost`
```

2. To use docker:
```bash
git clone https://github.com/almazkun/durls.git
cd durls
docker-compose up
docker-compose exec web python3 manage.py migrate

# Open your browser and navigate to `127.0.0.1` or `localhost`
```

3. To add a new redirect destination:
    - start the server
    - Open your browser and navigate to `127.0.0.1`
    - add a new slug and destination URL

### TODO
- Script to migrate and populate initial data to DB
- Job to reset the DB