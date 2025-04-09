# Quora like simple - Django Project

This is a simple Quora-like web application built using Django. It allows users to register, log in, post questions, answer them, like answers, and log out.

---

## Features

- User Registration
- User Login / Logout
- Post Questions
- View All Questions
- Answer Questions
- Like / Unlike Answers
- Simple UI using Django Templates

---

## Tech Stack

- Python 3.10.8
- Django 4.1.7
- SQLite (Default DB)
- Django Forms

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mohandas697/assignment.git
```

### 2. Set up virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Install dependencies

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (optional)

```bash
python manage.py createsuperuser
```

**OR**

Use the default user already created:

---

## Default Login Credentials

- **Username:** `mohan`
- **Password:** `123`

> You can log in at [http://127.0.0.1:8000/login/]

---

### 6. Run the server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## App Structure

- `quora/` - Main app with models, views, templates
- `templates/` - HTML templates for register, login, questions, etc.
- `forms.py` - Contains Django forms
- `models.py` - Question, Answer, Like models
- `urls.py` - URL mappings
- `views.py` - Core view logic for all user actions

---


## Author

Created by: Mohandas K 
