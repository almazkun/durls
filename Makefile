dev:
	pipenv run python3 manage.py runserver

test:
	pipenv run coverage run manage.py test
	pipenv run coverage report -m

prod:
	docker-compose -f docker-compose.prod.yml up -d --build 

migrate:
	docker-compose exec web python3 manage.py migrate

down:
	docker-compose down -v

demo:
	git checkout demo
	git pull origin main
	git push
	git checkout main
