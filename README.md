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
docker-compose up
# Open your browser and navigate to `127.0.0.1` or `localhost`
```

3. To add a new redirect destination:
    - start the server
    - Open your browser and navigate to `127.0.0.1:80/_/`
    - add a new slug and destination URL

### TODO

- .env to settings (allowed hosts, secret key, etc.)
- Script to migrate and populate initial data to DB
- Add DNS records
- Job to reset the DB