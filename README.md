# django_lab2

## Step 1: Create your project

> `django-admin startproject project_name`

## Step 2: Create your app
> `py manage.py startapp app_name`

## Step 3: Migrate first
> `py manage.py migrate`

## Step 4: Models Creation
1. Start by adding your models in the "models.py" file existing in the wanted application.
2. Add the app application in the "settings.py" file existing in the base folder
3. Make a migration of the models changes in order to be reflected into the database
> `py manage.py makemigrations app_name`
> `py manage.py migrate`

## Step 5: Create My Views
Many views would be needed.
1. A view to manage the departments
 . In this view, all the departments will be listed with a capacity to edit or even delete a department.
 . Also a button will be added in order to add a new department.
