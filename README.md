# Django_Scrapy_Integration
This repo contains the integrated django and scrapy project.
---

* The folder structure of the  project is a as follows:
  
|   ──** data**
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management
│   │   └── commands
│   │       └── scrape.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── ** my_project **
│   ├── asgi.py
│   ├── **crawler**
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       └── spider.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
└── scrapy.cfg

### Requirements:

To install requirements:
>* pip install -r requirements.txt



### Commands to follow for running project:
 
* Constructing Database & Data Tables
 >* ./manage.py makemigrations
 >* ./manage.py migrate

 * Creating admin credential
 >* ./manage.py createsuperuser

 * To run the scraper
 >* ./manage.py scrape

 * To run the django adminstration
     
 >* ./manage.py runserver