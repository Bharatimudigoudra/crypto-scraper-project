Create virtual environment:python -m venv venv
env activate: venv\Scripts\activate

create new django project:django-admin startproject crypto_scraper

Create new Django application:python manage.py startapp scraper


install necessary librarires: pip install -r requirements.txt

Set Up Redis for Celery:

Run Migration: python manage.py makemigrations
python manage.py migrate
python manage.py migrate django_celery_results

create and apply migration :python manage.py makemigrations scraper
python manage.py migrate


Create superuser(Optional):python manage.py createsuperuser

collect static files: python manage.py collectstatic

Run tests: python manage.py test

Inspect Project Structure: Display the project structure, including installed apps and middleware.

python manage.py showmigrations

Run celery Worker in separate terminal: # In a separate terminal, start the Celery worker
celery -A crypto_scraper worker --loglevel=info


Run the Django Project: # Start the Django server
python manage.py runserver
