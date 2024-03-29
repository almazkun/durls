dev:
	pipenv run python3 manage.py runserver

test:
	pipenv run coverage run manage.py test
	pipenv run coverage report -m

prod:
	docker-compose -f docker-compose.yml up -d --build

migrate:
	docker-compose exec -u ubuntu -T web python3 manage.py migrate

statics:
	docker-compose exec -u ubuntu -T web python3 manage.py collectstatic --noinput

demo_setup:
	docker-compose exec -u ubuntu -T web python3 manage.py demo_setup

down:
	docker-compose down -v

demo:
	git checkout demo
	git pull origin main
	git push
	git checkout main
