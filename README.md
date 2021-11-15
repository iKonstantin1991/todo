# Todo - Test task
Small api for application which helps to plan and control daily tasks
# Stack
Python 3.8, Django 3.0.5, Django REST Framework, PostgreSQL, Docker
# Commands to launch the app
- create .env file with:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Execute Commands:
- ```docker-composer up -d```
- ```docker-compose exec web python manage.py migrate --noinput```
- ```docker-compose exec web python manage.py collectstatic --no-input```

# Fill DB with test data:
- ```docker-compose exec web python manage.py loaddata testdata.json```

Superuser:
- username: kons
- password: easypass

or create another one:
- ```docker-compose exec web python manage.py createsuperuser```

# User rights:
### Admin(staff) users:
- Can create/get/edit/delete users<br>
admin user can create/delete another admin user but can not delete a superuser
- Can create/get/edit/delete all tasks

### Regular users:
- Can create tasks
- Can get tasks related to them(author or responsible)
- Can edit/delete tasks if user is author
- Can edit only status of tasks if user is responsible

# Endpoints and methods:
### - /api/users/<br>
available only to admin users<br>
methods: get, post
### - /api/users/id/<br>
available only to admin users<br>
methods: get, put, patch, delete

### - /api/auth/token/login/<br>
available to everyone<br>
methods: post
### - /api/auth/token/logout/<br>
available only to authentificated users<br>
methods: post


### - /api/tasks/<br>
available only to authentificated users<br>
methods: get, post
### - /api/tasks/id/<br>
available only to authentificated users<br>
methods: get, put/patch, delete

# Contacts
Email: ikonstantin1991@mail.ru<br>
Telegram: @ikonstantin91
