# 🧠 Recruiter-App Project

A role-based job listing and application backend built with Django and Django REST Framework. It features authentication, job management, and candidate applications, tailored for recruiters and candidates.

## 🚀 Features

- 🔐 **JWT Authentication** (via SimpleJWT)
- 👥 **Role-Based User Model**
  - `Recruiter` can create/manage jobs and view application stats
  - `Candidate` can apply to jobs
- ✉️ **Welcome Email on Registration**
- 🔐 **Forgot & Reset Password Functionality**
- 📄 **Job Posting Module**
  - Only recruiters can create/update/delete jobs
- 📨 **Job Applications**
  - Only candidates can apply
  - Prevent duplicate or late applications
- 📊 **Recruiter Dashboard**
  - See stats: total jobs, applications, hired, rejected
- ⚙️ **Custom Permissions** on all sensitive endpoints
- 🧪 **Swagger/OpenAPI Docs**
- ✅ Admin panel for managing all models

---

## 🛠️ Tech Stack

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- SimpleJWT  
- drf-yasg (for API documentation)  
- python-decouple  
- SQLite (for local dev)

---

## 📂 Project Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jobsite-backend.git
cd Recruiter-App

## 2. Create Virtual Environment
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Create a .env File
SECRET_KEY=your-django-secret-key
DEBUG=True

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=Recruiter App <your-email@example.com>

## 5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

## 6. Create a SuperAdmin
python manage.py createsuperuser

## 7. Run Development Server
python manage.py runserver

## 8. Visit Endpoints
Swagger/OpenAPI Docs: http://localhost:8000/swagger/
Admin Panel: http://localhost:8000/admin/
```

## Welcome Mail
![email send__](https://github.com/user-attachments/assets/c88d26a6-bfac-4296-bae5-c2d487b2fedc)

## Reset password Mail
![email send reset pass](https://github.com/user-attachments/assets/7f24821f-42d9-4ce2-996b-8d5a1a7a5ff5) 

## Recruiter Dashboard
![dashboard](https://github.com/user-attachments/assets/26e7d925-0db0-4dfd-9b5c-19daf70d4b58)





