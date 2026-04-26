# ============================================================
#  config.py – Application & Database Configuration
# ============================================================

class Config:
    # Flask secret key (change in production)
    SECRET_KEY = "hospital_secret_key_2025"

    # ── Admin Login Credentials ───────────────────────────────
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin@123"

    # ── MySQL connection settings ─────────────────────────────
    DB_HOST     = "localhost"
    DB_PORT     = 3306
    DB_USER     = "root"         # change to your MySQL username
    DB_PASSWORD = "root123"  # change to your MySQL password
    DB_NAME     = "hospital_db"