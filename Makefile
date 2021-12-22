run:
	pipenv run python3 manage.py runserver

run_d:
	docker build -t durls .
	docker run -d -p 80:80 durls