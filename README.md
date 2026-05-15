# Sensory 📸🎬

A personal media storage web app built with Django. Upload, organise, and browse your photos and videos — all behind a secure user account.

## Features
- User registration and login (Django Auth)
- Upload and store photos and videos locally
- Personal media library per user account
- Clean browsing interface

## Tech Stack
- **Backend:** Python, Django
- **Auth:** Django's built-in authentication system
- **Storage:** Local file system
- **Deployment:** Render

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation
```bash
git clone https://github.com/Riiode/Sensory.git
cd Sensory
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then visit `http://localhost:8000` in your browser.

### Create a superuser (optional)
```bash
python manage.py createsuperuser
```

## Live Demo
Deployed on Render: [sensory-jfh0.onrender.com](https://sensory-jfh0.onrender.com)

> Note: Running on Render's free tier — may take 30–60 seconds to spin up on first load.

## Project Status
Active. Planned additions: cloud storage integration, media tagging, and search.

## Author
**Ogheneriode** — [github.com/Riiode](https://github.com/Riiode)
