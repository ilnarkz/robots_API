install:
	pip install -r requirements.txt
start:
	python manage.py runserver 0.0.0.0:8000
migrate:
	python manage.py migrate
