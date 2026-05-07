# 🏥 Hospital Management System

A full-stack Hospital Management System developed using Python, Flask, MySQL, HTML, CSS, and JavaScript.

This project helps hospitals and clinics efficiently manage patient records, appointments, and healthcare operations through a clean and responsive web interface.

---

# 🚀 Features

* 🔐 Secure Admin Login System
* 👨‍⚕️ Patient Management
* ➕ Add New Patients
* ✏️ Edit Patient Details
* ❌ Delete Patient Records
* 📋 View All Patients
* 🔎 Search & Filter Functionality
* 📊 Dashboard Overview
* 💾 MySQL Database Integration
* 📱 Responsive User Interface
* ⚡ Flash Messages & Alerts

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

## Backend

* Python
* Flask

## Database

* MySQL

---

# 📂 Project Structure

```text
hospital_management/
│
├── app.py
├── config.py
├── hospital_database.sql
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── add_patient.html
│   ├── edit_patient.html
│   └── patients.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── models/
│   ├── patient_model.py
│   └── __init__.py
│
├── utils/
│   ├── database.py
│   └── __init__.py
│
└── __pycache__/
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/hospital-management-system.git
```

## 2️⃣ Open Project Folder

```bash
cd hospital-management-system
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

## Create MySQL Database

Run:

```bash
mysql -u root -p < hospital_database.sql
```

Or:

* Open MySQL Workbench
* Create a new SQL tab
* Import `hospital_database.sql`
* Execute the script

---

# 🔧 Configure Database

Open:

```python
config.py
```

Update your MySQL credentials:

```python
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'hospital_management'
```

---

# ▶️ Run The Project

```bash
python app.py
```

---

# 🌐 Open In Browser

```text
http://127.0.0.1:5000
```

---

# 📸 Main Modules

## 📊 Dashboard

* Total Patients Overview
* System Statistics
* Quick Access Navigation

## 👨‍⚕️ Patient Management

* Add Patients
* Edit Patient Information
* Delete Patients
* View Patient Records

## 🔍 Search System

* Search Patients
* Filter Data
* Quick Record Access

---

# ✨ UI Highlights

* Modern Responsive Design
* Clean Dashboard Layout
* Interactive Forms
* User-Friendly Navigation
* Mobile-Friendly Interface

---

# 🔒 Security Features

* Input Validation
* Secure Database Queries
* Session Management
* Protected Routes

---

# 📦 Requirements

Main dependencies:

* Flask
* mysql-connector-python
* Werkzeug

Install all packages:

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Improvements

* 📅 Appointment Scheduling
* 👨‍⚕️ Doctor Management
* 💊 Pharmacy Module
* 🧾 Billing System
* 📈 Analytics Dashboard
* 🌙 Dark Mode
* ☁️ Cloud Deployment

---

# 🧠 Learning Outcomes

This project demonstrates:

* Flask Web Development
* CRUD Operations
* MySQL Database Integration
* MVC Project Structure
* Responsive Frontend Design
* Backend Routing & APIs

---

# 🏷️ GitHub Topics

```text
flask python mysql hospital-management healthcare-management patient-management fullstack-webapp responsive-design
```

---

# 👨‍💻 Author

GOBINDA CHANDRA PANDA

---

# 📜 License

This project is open-source and free to use for educational purposes.

---

# ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 🛠️ Contribute improvements

---

# 📬 Contact

Feel free to connect for feedback and collaboration.
