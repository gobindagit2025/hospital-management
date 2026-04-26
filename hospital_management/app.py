# ============================================================
#  app.py – Main Flask Application
#  Run: python app.py
# ============================================================

from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from config import Config
from models.patient_model import (
    get_all_patients,
    get_patient_by_id,
    get_dashboard_stats,
    add_patient,
    update_patient,
    delete_patient,
)

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

# ── Admin Credentials (stored in config, changeable at runtime) ──
ADMIN_CREDENTIALS = {
    "username": Config.ADMIN_USERNAME,
    "password": Config.ADMIN_PASSWORD,
}


# ── Auth Helpers ─────────────────────────────────────────────

def login_required(f):
    """Decorator: redirect to login if admin is not authenticated."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin_logged_in"):
            flash("Please log in to access the admin panel.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


# ── Form Helper ──────────────────────────────────────────────

def collect_form_data(form) -> dict:
    """Extract and clean patient form fields from request.form."""
    return {
        "patient_name"  : form.get("patient_name", "").strip(),
        "age"           : form.get("age", 0),
        "gender"        : form.get("gender", ""),
        "blood_group"   : form.get("blood_group", "").strip(),
        "doctor_name"   : form.get("doctor_name", "").strip(),
        "disease"       : form.get("disease", "").strip(),
        "admission_date": form.get("admission_date", ""),
        "checkup_date"  : form.get("checkup_date", "") or None,
        "discharged"    : form.get("discharged", "No"),
        "discharge_date": form.get("discharge_date", "") or None,
    }


# ── Auth Routes ──────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    """Admin login page."""
    if session.get("admin_logged_in"):
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if (username == ADMIN_CREDENTIALS["username"] and
                password == ADMIN_CREDENTIALS["password"]):
            session["admin_logged_in"] = True
            session["admin_username"] = username
            flash("Welcome back, Admin!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password. Please try again.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out the admin."""
    session.clear()
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("login"))


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow admin to change their password."""
    if request.method == "POST":
        current_password = request.form.get("current_password", "")
        new_password     = request.form.get("new_password", "")
        confirm_password = request.form.get("confirm_password", "")

        if current_password != ADMIN_CREDENTIALS["password"]:
            flash("Current password is incorrect.", "error")
        elif len(new_password) < 6:
            flash("New password must be at least 6 characters long.", "error")
        elif new_password != confirm_password:
            flash("New password and confirm password do not match.", "error")
        elif new_password == current_password:
            flash("New password must be different from the current password.", "error")
        else:
            ADMIN_CREDENTIALS["password"] = new_password
            flash("Password changed successfully!", "success")
            return redirect(url_for("dashboard"))

    return render_template("change_password.html")


# ── Protected Routes ─────────────────────────────────────────

@app.route("/")
@login_required
def dashboard():
    """Home page – summary statistics."""
    stats = get_dashboard_stats()
    recent_patients = get_all_patients()[:5]   # latest 5
    return render_template("dashboard.html", stats=stats, patients=recent_patients)


@app.route("/patients")
@login_required
def patients():
    """List all patients with optional search / filter."""
    search        = request.args.get("search", "").strip()
    status_filter = request.args.get("status", "")
    all_patients  = get_all_patients(search=search, status_filter=status_filter)
    return render_template(
        "patients.html",
        patients      = all_patients,
        search        = search,
        status_filter = status_filter,
    )


@app.route("/add_patient", methods=["GET", "POST"])
@login_required
def add_patient_route():
    """Add a new patient record."""
    if request.method == "POST":
        data = collect_form_data(request.form)

        # Basic validation
        if not data["patient_name"] or not data["admission_date"]:
            flash("Patient name and admission date are required.", "error")
            return render_template("add_patient.html", form_data=data)

        try:
            add_patient(data)
            flash(f"Patient '{data['patient_name']}' added successfully!", "success")
            return redirect(url_for("patients"))
        except Exception as e:
            flash(f"Database error: {e}", "error")
            return render_template("add_patient.html", form_data=data)

    return render_template("add_patient.html", form_data={})


@app.route("/edit_patient/<int:patient_id>", methods=["GET", "POST"])
@login_required
def edit_patient_route(patient_id):
    """Edit an existing patient record."""
    patient = get_patient_by_id(patient_id)
    if not patient:
        flash("Patient not found.", "error")
        return redirect(url_for("patients"))

    if request.method == "POST":
        data = collect_form_data(request.form)

        if not data["patient_name"] or not data["admission_date"]:
            flash("Patient name and admission date are required.", "error")
            return render_template("edit_patient.html", patient=patient)

        try:
            update_patient(patient_id, data)
            flash(f"Patient '{data['patient_name']}' updated successfully!", "success")
            return redirect(url_for("patients"))
        except Exception as e:
            flash(f"Database error: {e}", "error")
            return render_template("edit_patient.html", patient=patient)

    return render_template("edit_patient.html", patient=patient)


@app.route("/delete_patient/<int:patient_id>", methods=["POST"])
@login_required
def delete_patient_route(patient_id):
    """Delete a patient record (POST only for safety)."""
    patient = get_patient_by_id(patient_id)
    if patient:
        try:
            delete_patient(patient_id)
            flash(f"Patient '{patient['patient_name']}' deleted.", "success")
        except Exception as e:
            flash(f"Delete failed: {e}", "error")
    else:
        flash("Patient not found.", "error")
    return redirect(url_for("patients"))


# ── Entry Point ──────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)