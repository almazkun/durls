run:
	pipenv run python3 manage.py runserver

run_d: 
	docker build -t durls .
	docker run --rm -d -p 80:8000 durls

stop:
	docker stop $(shell docker ps -aq)
