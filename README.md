# Healthcare Backend API

A RESTful backend system for a healthcare application built with **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT Authentication**.

## 🚀 Features

- Custom email-based user authentication with JWT tokens
- Full CRUD for Patient and Doctor management
- Patient-Doctor mapping/assignment system
- Secure endpoints (authentication required)
- PostgreSQL database with Django ORM
- Environment variable-based configuration
- CORS support

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Django 5.x | Web framework |
| Django REST Framework | API layer |
| djangorestframework-simplejwt | JWT Authentication |
| PostgreSQL | Database |
| psycopg2-binary | PostgreSQL adapter |
| python-dotenv | Environment variables |
| django-cors-headers | CORS handling |

## 📁 Project Structure

```
healthcare-backend/
├── healthcare/          # Django project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/            # User registration & login
│   ├── models.py        # Custom User model
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── patients/            # Patient management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── doctors/             # Doctor management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── mappings/            # Patient-Doctor assignments
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── .env                 # Environment variables (not committed)
├── .env.example         # Example env file
├── requirements.txt
└── manage.py
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd healthcare-backend
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and fill in your values:
```bash
cp .env.example .env
```

Edit `.env`:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Create PostgreSQL database
```sql
CREATE DATABASE healthcare_db;
```

### 6. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the development server
```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/auth/register/` | Register a new user | ❌ |
| POST | `/api/auth/login/` | Login and get JWT tokens | ❌ |

### Patients

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/patients/` | Create a patient | ✅ |
| GET | `/api/patients/` | List your patients | ✅ |
| GET | `/api/patients/<id>/` | Get patient details | ✅ |
| PUT | `/api/patients/<id>/` | Update a patient | ✅ |
| DELETE | `/api/patients/<id>/` | Delete a patient | ✅ |

### Doctors

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/doctors/` | Add a doctor | ✅ |
| GET | `/api/doctors/` | List all doctors | ✅ |
| GET | `/api/doctors/<id>/` | Get doctor details | ✅ |
| PUT | `/api/doctors/<id>/` | Update a doctor | ✅ |
| DELETE | `/api/doctors/<id>/` | Delete a doctor | ✅ |

### Patient-Doctor Mappings

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/mappings/` | Assign doctor to patient | ✅ |
| GET | `/api/mappings/` | List all mappings | ✅ |
| GET | `/api/mappings/patient/<patient_id>/` | Doctors for a patient | ✅ |
| DELETE | `/api/mappings/<id>/delete/` | Remove assignment | ✅ |

---

## 🔑 Authentication

All protected endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

Get tokens by registering or logging in. Tokens expire after **1 day** (access) and **7 days** (refresh).

---

## 📬 Sample API Requests

### Register
```json
POST /api/auth/register/
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

### Login
```json
POST /api/auth/login/
{
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

### Create Patient
```json
POST /api/patients/
Authorization: Bearer <token>
{
  "name": "Jane Smith",
  "age": 35,
  "gender": "F",
  "blood_group": "O+",
  "phone": "9876543210",
  "address": "123 Main St, Delhi",
  "medical_history": "Diabetes Type 2"
}
```

### Create Doctor
```json
POST /api/doctors/
Authorization: Bearer <token>
{
  "name": "Rahul Sharma",
  "specialization": "Cardiology",
  "email": "dr.rahul@hospital.com",
  "phone": "9876543210",
  "experience_years": 10,
  "hospital": "Apollo Hospital"
}
```

### Assign Doctor to Patient
```json
POST /api/mappings/
Authorization: Bearer <token>
{
  "patient": 1,
  "doctor": 1,
  "notes": "Follow-up needed in 2 weeks"
}
```
