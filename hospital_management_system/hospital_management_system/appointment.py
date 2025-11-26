# ============================
#       APPOINTMENT CLASS
# ============================

from utils import generate_id

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.id = generate_id("APT")  # Auto ID: APT123
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        return (
            f"{self.id} | Patient: {self.patient.name} | "
            f"Doctor: {self.doctor.name} | Date: {self.date} | Time: {self.time}"
        )
