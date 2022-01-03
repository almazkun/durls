run:
	sudo pipenv run python3 manage.py runserver 127.0.0.1:80

run_d: 
	docker-compose up --build

test:
	pipenv run coverage run manage.py test
	pipenv run coverage report -m

prod:
	docker-compose -f docker-compose.prod.yml up -d --build 

migrate:
	docker-compose exec -ti web python manage.py migrate
	exit 0

down:
	docker-compose down -v