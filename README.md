# Django Task Manager

A simple task manager built with Python, HTML, and Django. It lets you add tasks, edit them, mark them complete, and delete them. Clean templates and a minimal CSS file make it easy to understand and extend.

## Features
- Add tasks with title and optional description
- Edit existing tasks
- Toggle complete/incomplete
- Delete tasks
- SQLite database, Django admin enabled

## Tech Stack
- Python 3
- Django 5.x (compatible with 4.2+)
- HTML templates, static CSS
- SQLite (default)

## Quickstart
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit `http://127.0.0.1:8000/`.

## Project Structure
```
manage.py
requirements.txt
.gitignore
static/
  css/styles.css
templates/
  base.html
  tasks/
    task_list.html
    task_edit.html
    task_confirm_delete.html
taskmanager/
  settings.py
  urls.py
  asgi.py
  wsgi.py
tasks/
  models.py
  views.py
  forms.py
  urls.py
  admin.py
```

## Notes
- For production, set `DEBUG=False` and configure `ALLOWED_HOSTS` in `taskmanager/settings.py`.
- Optionally set `DJANGO_SECRET_KEY` in your environment.

## Short Description
A minimal, beginner-friendly Django application to manage tasks (create, edit, toggle complete, delete) using SQLite, server-rendered templates, and simple styling.