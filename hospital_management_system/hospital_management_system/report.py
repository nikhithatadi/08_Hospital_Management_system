# ============================
#        REPORT MODULE
# ============================

def doctor_schedule_report(doctor):
    """
    Generate and print schedule report for a doctor.
    doctor.schedule contains list of datetime objects.
    Appointment objects will be shown cleanly.
    """
    print(f"\n=== Doctor Schedule Report ===")
    print(f"Doctor: {doctor.name} ({doctor.specialization})")
    print("------------------------------------")

    if not doctor.schedule:
        print("No appointments scheduled.")
        return

    for appt_time in sorted(doctor.schedule):
        print(f"🕒 Appointment Time: {appt_time}")


def patient_appointments_report(patient, appointments):
    """
    Show all appointments of a given patient.
    appointments: list of Appointment objects
    """
    print(f"\n=== Patient Appointment History ===")
    print(f"Patient: {patient.name} (Age: {patient.age})")
    print("------------------------------------")

    patient_appts = [a for a in appointments if a.patient.id == patient.id]

    if not patient_appts:
        print("No appointments found.")
        return

    for appt in patient_appts:
        print(f"{appt.id} | Doctor: {appt.doctor.name} | Time: {appt.date_time}")
