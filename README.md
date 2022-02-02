# Search for a Movie

Mini web applications helping users to choose movies to watch

## Project Description
Use IMDB database 

Use virtual environment [venv](https://docs.python.org/3/library/venv.html) to encapsulate packages used

Use the web framework [Django](https://www.djangoproject.com/) to build project

Use Django application [django_import_export](https://django-import-export.readthedocs.io/en/latest/) to import data from database excel sheet 

Use Django application [django_filter](https://django-filter.readthedocs.io/en/stable/) to filter down a queryset based on a model’s fields

mostly search parameters use greater than or equal methodology for filtering


## Installation

For Ubuntu user , git clone the repository

```bash
git clone https://github.com/Aya262/task2.git
```
change directory to task2 on device 
and activate virtualenv

```bash
~/task2-master$ source env/bin/activate
```
navigate to manage.py location and run server
```bash
(env) aya@aya-Inspiron-5559:~/task2-master/tasks$ python manage.py runserver
```
In browser go to local host "http://127.0.0.1:8000/"



# Data Parsing

Small software which can parse CSV, XML,
XLSX to Json

## program

Use the Pandas library [pandas](https://pandas.pydata.org/) for conversion

Contain simple form to upload file and choose file format 

Access the program through the same steps above except the url : "http://127.0.0.1:8000/parse/"
