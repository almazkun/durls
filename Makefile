run:
	pipenv run python3 manage.py runserver

run_d: 
	docker-compose up -d --build

stop:
	docker-compose down -v

test:
	coverage run manage.py test
	coverage report -m