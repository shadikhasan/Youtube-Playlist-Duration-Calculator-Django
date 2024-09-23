[Live](https://youtube-playlist-duration-calculator.onrender.com)

![Screenshot (31)](https://github.com/user-attachments/assets/a91d79e9-bc42-4d7d-9802-875b25a9f455)
![Screenshot (32)](https://github.com/user-attachments/assets/e791fc32-15cb-4934-a0d5-22f759f88cd2)

# 1. Initial Setup

## Prerequisites
Make sure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, if using Docker)
- **Git** (version control)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine and navigate to the project directory:

```
git clone https://github.com/shadikhasan/Youtube-Playlist-Duration-Calculator-Django.git
cd Youtube Playlist Duration Calculator Django
```

### 2. Create a Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```
python manage.py migrate
```

### 5.1. Create a Superuser (Optional)

```
python manage.py createsuperuser
```

### 5.2 Initial super user by command(Optional)

```
python manage.py init_superuser
```

### 6. Start the Development Server

```
python manage.py runserver
```

The API will then be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# 2. Using docker

### Build Docker file

```
docker-compose build
```

### To start project, run:

```
docker-compose up
```

The API will then be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### To Log in To the Dashboard(Frontend) or Admin Panel

#### Username

```
admin
```

#### Password

```
admin
```

---

## Development Guide

### Create Project

```
docker-compose run app sh -c "django-admin startproject NewProject ."
```

### Create New App

```
docker-compose run --rm app sh -c "python manage.py startapp newApp"
```

### Create Super User

```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### Initial super user by command(Optional)

```
docker-compose run --rm app sh -c "python manage.py init_superuser"
```

### Make Migrations

```
docker-compose run app sh -c "python manage.py makemigrations"
```
