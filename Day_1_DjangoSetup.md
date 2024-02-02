# Requirements for Django:

- Git Installed? V-
- VS Code Installed V-
- Python Version V-
- pip Version V-

- Python Virtual Environment Check: What was used in PCEP Course? (conda, virutalenv, pyenv, pipenv, venv) 
Official Virtual Environment venv: https://docs.python.org/3/tutorial/venv.html

or use pipenv virtual environment:
pip3 install pipenv
pipenv install django==4.1
pipenv shell
exit

===
# Linux:
https://www.lpi.org/our-certifications/lpic-1-overview/ 

# Markdown:
===
- Tutorial: https://www.markdowntutorial.com/
- Markdown Cheatsheet: https://www.markdownguide.org/cheat-sheet/
- Github Markdown Reference: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- Django by Example (Paackt Publishing): https://github.com/PacktPublishing/Django-4-by-example

# Python Reference:
- https://www.w3schools.com/python/python_dictionaries.asp
- https://www.geeksforgeeks.org/


# Django Tutorials
- Polls App: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
- Library App: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website

# Django Docs:
- https://docs.djangoproject.com/en/4.2/ or pdf: https://media.readthedocs.org/pdf/django/4.2.x/django.pdf
- https://www.w3schools.com/django/

# Books:
- Django Book
- Django 4 by Example

Django:
===

# Install PIP:
mac: python -m ensurepip --upgrade
win: py -m ensurepip --upgrade

# Tree command:
brew install tree


# Install Django
pip install django
pip install Django==5.0.1

## Check Django Version:
---
python
import django
django.VERSION
exit()
---
python -c "import django; print(django.get_version())"
---
# Django useing Virtual Environment venv:

First, create the virtual environment:
python3 -m venv django-env

Then, use this environment:

In mac:
source django-env/bin/activate

In cmd.exe
venv\Scripts\activate.bat
In PowerShell
venv\Scripts\Activate.ps1


Next, install django
python -m pip install django

Finally test django is working
django-admin startproject mysite

Deactivate the virtual environment:
deactivate 

If the above deactivation does not work then try:
source deactivate
--- 

# Start django project
pipenv install django==2.1
pipenv shell
django-admin startproject test_project .
python manage.py runserver

---
Flask vs Django:  https://wsvincent.com/flask-vs-django/
---

# Django Apps:
- A djago project can contain multiple apps
- project level vs app level

```python
python manage.py startapp pages
```

manually add apps to settings of project

# Views URLConfs
Django Request/Response Cycle: URL -> View -> Model (typically) -> Template

# Add an About page to our website

## Templates
Teamples, Views, and URLs make up a webpage

URL: control initial route, entry point into a page such as /about
View: contains the logic or what to display from the model/database
Template: has HTML with variables

## Django Class-based-Views
function vs class based views

# Django Official Pages:
- Django WebApp: https://docs.djangoproject.com/en/4.2/ref/
- Django API: https://www.django-rest-framework.org

# Day 1 Django Homework:
- Homework: read page 431-433 of Python Cookbook 3rd Edition
- Homework: read first chapter of django book

Kill port: sudo lsof -t -i tcp:8000 | xargs kill -9

# Added github link:
https://github.com/primecarecorp/202310CEIWDX_AZ-204

# Those who want to get ahead: (this Friday or next Monday)
Install Docker Desktop: 
- Windows: https://docs.docker.com/desktop/install/windows-install/
- Mac: https://docs.docker.com/desktop/install/mac-install/
  
Docker Tutorials: https://www.docker.com/play-with-docker/
