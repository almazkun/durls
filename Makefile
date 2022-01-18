dev:
	docker build -t durls_image .
	docker run --rm -p 80:80 --mount type=bind,source="$(shell pwd)",target=/usr/src/code --name durls durls_image python manage.py runserver 0.0.0.0:80

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
