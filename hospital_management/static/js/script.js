/* ============================================================
   MediCore HMS – script.js
   Handles: delete confirmation, discharge date toggle,
            auto-dismiss flash messages, date validation
   ============================================================ */

"use strict";

/* ── Delete Confirmation ───────────────────────────────────── */

/**
 * Called via onsubmit on delete forms.
 * Returns true (allow submit) or false (cancel).
 * @param {string} name - Patient name to display
 */
function confirmDelete(name) {
    return window.confirm(
        `Are you sure you want to delete "${name}"?\n\nThis action cannot be undone.`
    );
}


/* ── Discharge Date Toggle ─────────────────────────────────── */

/**
 * Show/hide the discharge date field depending on
 * the discharged select value.
 */
function toggleDischargeDate() {
    const select = document.getElementById("dischargedSelect");
    const group  = document.getElementById("dischargeDateGroup");
    if (!select || !group) return;

    if (select.value === "Yes") {
        group.style.display = "block";
        group.style.animation = "slideIn .2s ease";
    } else {
        group.style.display = "none";
        // Clear the date so it won't be submitted accidentally
        const input = group.querySelector("input[type='date']");
        if (input) input.value = "";
    }
}

// Run on page load so edit form reflects current state
document.addEventListener("DOMContentLoaded", function () {
    toggleDischargeDate();
    initDateValidation();
    initFlashAutoDismiss();
    highlightActiveNav();
});


/* ── Date Validation ───────────────────────────────────────── */

function initDateValidation() {
    const form = document.getElementById("patientForm");
    if (!form) return;

    form.addEventListener("submit", function (e) {
        const admissionInput = form.querySelector("input[name='admission_date']");
        const dischargeInput = form.querySelector("input[name='discharge_date']");

        if (!admissionInput) return;

        const admDate = new Date(admissionInput.value);
        const today   = new Date();
        today.setHours(0, 0, 0, 0);

        if (admDate > today) {
            e.preventDefault();
            showInlineError(admissionInput, "Admission date cannot be in the future.");
            return;
        }

        if (dischargeInput && dischargeInput.value) {
            const disDate = new Date(dischargeInput.value);
            if (disDate < admDate) {
                e.preventDefault();
                showInlineError(dischargeInput, "Discharge date must be after admission date.");
                return;
            }
        }
    });
}

/**
 * Display a small error message under a form input.
 * @param {HTMLElement} input
 * @param {string} message
 */
function showInlineError(input, message) {
    // Remove existing error
    const existing = input.parentElement.querySelector(".field-error");
    if (existing) existing.remove();

    const err = document.createElement("span");
    err.className = "field-error";
    err.style.cssText = "display:block;color:#dc2626;font-size:.78rem;margin-top:4px;";
    err.textContent = message;

    input.style.borderColor = "#dc2626";
    input.parentElement.appendChild(err);
    input.focus();

    // Auto-clear after 4 s
    setTimeout(() => {
        err.remove();
        input.style.borderColor = "";
    }, 4000);
}


/* ── Flash Auto-Dismiss ────────────────────────────────────── */

function initFlashAutoDismiss() {
    const flashes = document.querySelectorAll(".flash");
    flashes.forEach(function (el) {
        setTimeout(function () {
            el.style.transition = "opacity .4s ease";
            el.style.opacity    = "0";
            setTimeout(() => el.remove(), 420);
        }, 4000); // dismiss after 4 s
    });
}


/* ── Active Nav Highlight (redundant guard) ─────────────────── */

function highlightActiveNav() {
    const links   = document.querySelectorAll(".nav-link");
    const current = window.location.pathname;

    links.forEach(function (link) {
        const href = link.getAttribute("href");
        if (href && current === href) {
            link.classList.add("active");
        }
    });
}
