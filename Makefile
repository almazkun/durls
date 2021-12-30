run:
	pipenv run python3 manage.py runserver

run_d: 
	docker-compose up --build

stop:
	docker-compose down -v

test:
	pipenv run coverage run manage.py test
	pipenv run coverage report -m

prod:
	docker-compose -f docker-compose.prod.yml up -d --build 