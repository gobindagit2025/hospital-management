-- ============================================================
--  Hospital Management System - Database Setup
--  Database: hospital_db
--  Compatible with: MySQL Workbench / MySQL 8.x
-- ============================================================

-- Create and select the database
CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- ============================================================
--  TABLE: patients
-- ============================================================
CREATE TABLE IF NOT EXISTS patients (
    id              INT             AUTO_INCREMENT PRIMARY KEY,
    patient_name    VARCHAR(100)    NOT NULL,
    age             INT             NOT NULL,
    gender          ENUM('Male', 'Female', 'Other') NOT NULL,
    blood_group     VARCHAR(5)      NOT NULL,
    doctor_name     VARCHAR(100)    NOT NULL,
    disease         VARCHAR(200)    NOT NULL,
    admission_date  DATE            NOT NULL,
    checkup_date    DATE,
    discharged      ENUM('Yes', 'No') NOT NULL DEFAULT 'No',
    discharge_date  DATE,
    created_at      TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
--  SAMPLE DATA
-- ============================================================
INSERT INTO patients
    (patient_name, age, gender, blood_group, doctor_name, disease,
     admission_date, checkup_date, discharged, discharge_date)
VALUES
    ('Aarav Sharma',   34, 'Male',   'B+',  'Dr. Priya Nair',    'Typhoid Fever',     '2025-03-01', '2025-03-05', 'Yes', '2025-03-10'),
    ('Meera Iyer',     28, 'Female', 'O+',  'Dr. Rahul Mehta',   'Appendicitis',      '2025-03-10', '2025-03-12', 'Yes', '2025-03-17'),
    ('Rohan Desai',    45, 'Male',   'A+',  'Dr. Sunita Joshi',  'Diabetes Type 2',   '2025-04-01', '2025-04-06', 'No',  NULL),
    ('Kavya Reddy',    22, 'Female', 'AB-', 'Dr. Amit Kapoor',   'Viral Pneumonia',   '2025-04-05', '2025-04-08', 'No',  NULL),
    ('Arjun Patel',    55, 'Male',   'O-',  'Dr. Priya Nair',    'Hypertension',      '2025-04-10', '2025-04-13', 'No',  NULL),
    ('Divya Nair',     31, 'Female', 'B-',  'Dr. Rahul Mehta',   'Migraine',          '2025-04-12', '2025-04-14', 'Yes', '2025-04-16'),
    ('Kiran Joshi',    60, 'Male',   'A-',  'Dr. Sunita Joshi',  'Cardiac Arrhythmia','2025-04-15', '2025-04-18', 'No',  NULL),
    ('Ananya Singh',   19, 'Female', 'B+',  'Dr. Amit Kapoor',   'Dengue Fever',      '2025-04-18', '2025-04-20', 'No',  NULL);
