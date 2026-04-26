# MediCore – Hospital Management System

A full-stack Hospital Management System built with **Flask**, **MySQL**, and a modern HTML/CSS/JS frontend.

---

## Project Structure

```
hospital_management/
├── app.py                    ← Flask application entry point
├── config.py                 ← Database & app configuration
├── requirements.txt          ← Python dependencies
├── hospital_database.sql     ← MySQL schema + sample data
├── models/
│   ├── __init__.py
│   └── patient_model.py      ← CRUD functions for patients
├── utils/
│   ├── __init__.py
│   └── database.py           ← MySQL connection helpers
├── templates/
│   ├── base.html             ← Shared layout & navigation
│   ├── dashboard.html        ← Statistics + recent patients
│   ├── patients.html         ← Patient list with search/filter
│   ├── add_patient.html      ← New patient form
│   └── edit_patient.html     ← Edit patient form
└── static/
    ├── css/style.css         ← Complete UI stylesheet
    └── js/script.js          ← Dynamic interactions
```

---

## Quick Setup

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up the MySQL database
Open **MySQL Workbench** (or any MySQL client) and run:
```bash
mysql -u root -p < hospital_database.sql
```
Or paste the contents of `hospital_database.sql` into MySQL Workbench and execute.

### 3. Configure database credentials
Edit **`config.py`**:
```python
DB_USER     = "root"           # your MySQL username
DB_PASSWORD = "your_password"  # your MySQL password
```

### 4. Run the application
```bash
python app.py
```

Open your browser at: **http://localhost:5000**

---

## Features

| Feature | Details |
|---|---|
| Dashboard | Total / Admitted / Discharged counts + recent patients |
| Add Patient | Full registration form with date validation |
| Edit Patient | Update any patient detail |
| Delete Patient | Confirmation dialog before deletion |
| Search | Filter patients by name |
| Status Filter | Show All / Admitted / Discharged |
| Status Badges | 🟢 Discharged · 🔴 Admitted |
| Responsive UI | Works on desktop & tablet |

---

## Routes

| URL | Method | Description |
|---|---|---|
| `/` | GET | Dashboard |
| `/patients` | GET | List all patients (search/filter) |
| `/add_patient` | GET / POST | Add new patient |
| `/edit_patient/<id>` | GET / POST | Edit patient |
| `/delete_patient/<id>` | POST | Delete patient |
