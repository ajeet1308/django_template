Django Installation Process:

# Installing pip using python3
>> sudo apt-get install python3-pip


# Creating an virtual env using pip
>> sudo pip3 install virtualenv
>> virtualenv venv
>> source venv/bin/activate
>> deactivate

# Installing Django dependecies
>> pip install Django
>> django-admin --version

# Creating Django Project
>> django-admin startproject <projectName>
>> python manage.py runserver

# Uninstall Django from separate environment
- Go to current environment and activate it
>> pip uninstall django
- Now uninstall virtual environment which is currently active after deactivating it
deactivate
>> sudo rm -rf venv

# To save installed version in rquirements.txt file
>> pip freeze > requirements.txt

# To install required version present in requirements.txt file
>> pip install -r requirements.txt

# How to Start/Create a new application
>> python manage.py startapp <appName>

# How to Install Application in our Project after creating it
- Creating application is not enough we have also to install application in our project
- We install application in our project settings.py file, this is cumpulsory otherwise Application won't be recongnized by Django
In Settings.py file :
@code  INSTALLED_APPS = [
    django.contrib.admin,....,
    '<applicationName 1>'
    '<applicationName 2>
]

# Migrations
>> python manage.py makemigrations

# Migrate
>> python manage.py migrate

# List down all migrations status
>> python manage.py showmigrations

# create super user
>> python manage.py createsuperuser