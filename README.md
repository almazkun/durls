# durls
**D**jango **URL** **S**hortener

## Demo at:
https://durls.akun.dev/

## Usage
1. Start development server:
```bash
git clone https://github.com/almazkun/durls.git
cd durls
pipenv install
pipenv shell
python3 manage.py migrate
python3 manage.py runserver 127.0.0.1:8000

# Open your browser and navigate to `127.0.0.1:8000` or `localhost:8000`
```

2. Start production server:
```bash
git clone https://github.com/almazkun/durls.git
cd durls
docker-compose up -d --build
docker-compose exec web python3 manage.py migrate

# Open your browser and navigate to `127.0.0.1` or `localhost`
```

3. To add a new redirect destination:
    - Start the server
    - Open your browser and navigate to `127.0.0.1` or pointed domain. 
    - Create a user and add a new redirect destination.

### TODO
- Permission for admin to manage all destinations
- Script to migrate and populate initial data to DB
- Job to reset the DB
- Social login