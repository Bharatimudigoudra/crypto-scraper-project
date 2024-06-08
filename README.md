# Crypto Scraper Project

Crypto Scraper is a Django application designed to scrape cryptocurrency data from the CoinMarketCap website. This project uses Django, Celery, and Selenium with Microsoft Edge WebDriver for scraping the data.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Node.js (for frontend dependencies, if any)
- Redis (for Celery backend)

### Step-by-Step Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crypto-scraper-project.git
   cd crypto-scraper-project

Create a virtual environment and activate it:
python -m venv venv
# On Windows, use `venv\Scripts\activate`

Install the required Python packages:
pip install -r requirements.txt

Install msedge-selenium-tools package for Microsoft Edge WebDriver:
pip install msedge-selenium-tools selenium

Make migrations and migrate the database:
python manage.py makemigrations
python manage.py migrate

Create a superuser for the Django admin:
python manage.py createsuperuser

Install and run Redis server:
Follow the Redis installation guide to install Redis on your system and start the server.

Setup
Configure Django Settings
Update your crypto_scraper/settings.py to include the necessary configurations:

INSTALLED_APPS = [
    ...
    'scraper',
    'rest_framework',
    'django_celery_results',
]

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

Configure Microsoft Edge WebDriver
In scraper/utils.py, configure the WebDriver to use Microsoft Edge:
from msedge.selenium_tools import Edge, EdgeOptions
from msedge.selenium_tools import EdgeChromiumDriverManager

options = EdgeOptions()
options.use_chromium = True

driver_path = EdgeChromiumDriverManager().install()
driver = Edge(executable_path=driver_path, options=options)

Running the Project
Start Django Development Server
Run the following command to start the Django development server:
python manage.py runserver

Start Celery Worker
Open another terminal and start the Celery worker:
celery -A crypto_scraper worker --loglevel=info

Usage
Starting a Scraping Job
Send a POST request to /api/start-scraping/ with the list of cryptocurrency acronyms you want to scrape.
{
    "coins": ["BTC", "ETH", "LTC"]
}

Checking Scraping Job Status
Send a GET request to /api/scraping-status/{job_id}/ to check the status of a scraping job.

Programming stucture
crypto-scraper-project/
│
├── crypto_scraper/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── scraper/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md

License
This project is licensed under the MIT License. See the LICENSE file for more information.
sql>>
This `README.md` provides detailed steps for setting up, configuring, and running your Django Crypto Scraper project with Microsoft Edge WebDriver, using inline code blocks for clarity. Adjust the repository URL and other project-specific details as necessary.

