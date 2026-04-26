# ============================================================
#  models/patient_model.py – CRUD operations for patients
# ============================================================

from utils.database import execute_query


# ── READ ─────────────────────────────────────────────────────

def get_all_patients(search: str = "", status_filter: str = ""):
    """
    Fetch patients with optional name search and discharge filter.
    Returns list of dicts.
    """
    query  = "SELECT * FROM patients WHERE 1=1"
    params = []

    if search:
        query  += " AND patient_name LIKE %s"
        params.append(f"%{search}%")

    if status_filter in ("Yes", "No"):
        query  += " AND discharged = %s"
        params.append(status_filter)

    query += " ORDER BY created_at DESC"
    return execute_query(query, tuple(params), fetch=True)


def get_patient_by_id(patient_id: int):
    """Return a single patient dict or None."""
    rows = execute_query(
        "SELECT * FROM patients WHERE id = %s",
        (patient_id,),
        fetch=True
    )
    return rows[0] if rows else None


def get_dashboard_stats():
    """Return total, admitted, and discharged counts."""
    rows = execute_query(
        """
        SELECT
            COUNT(*)                                   AS total,
            SUM(discharged = 'No')                     AS admitted,
            SUM(discharged = 'Yes')                    AS discharged
        FROM patients
        """,
        fetch=True
    )
    return rows[0] if rows else {"total": 0, "admitted": 0, "discharged": 0}


# ── CREATE ───────────────────────────────────────────────────

def add_patient(data: dict):
    """Insert a new patient. Returns the new row's id."""
    query = """
        INSERT INTO patients
            (patient_name, age, gender, blood_group, doctor_name,
             disease, admission_date, checkup_date, discharged, discharge_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        data["patient_name"],
        data["age"],
        data["gender"],
        data["blood_group"],
        data["doctor_name"],
        data["disease"],
        data["admission_date"],
        data.get("checkup_date") or None,
        data["discharged"],
        data.get("discharge_date") or None,
    )
    return execute_query(query, params)


# ── UPDATE ───────────────────────────────────────────────────

def update_patient(patient_id: int, data: dict):
    """Update an existing patient record."""
    query = """
        UPDATE patients SET
            patient_name   = %s,
            age            = %s,
            gender         = %s,
            blood_group    = %s,
            doctor_name    = %s,
            disease        = %s,
            admission_date = %s,
            checkup_date   = %s,
            discharged     = %s,
            discharge_date = %s
        WHERE id = %s
    """
    params = (
        data["patient_name"],
        data["age"],
        data["gender"],
        data["blood_group"],
        data["doctor_name"],
        data["disease"],
        data["admission_date"],
        data.get("checkup_date") or None,
        data["discharged"],
        data.get("discharge_date") or None,
        patient_id,
    )
    execute_query(query, params)


# ── DELETE ───────────────────────────────────────────────────

def delete_patient(patient_id: int):
    """Permanently remove a patient record."""
    execute_query("DELETE FROM patients WHERE id = %s", (patient_id,))
