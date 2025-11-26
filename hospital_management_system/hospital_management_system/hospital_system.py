# ============================
#   HOSPITAL SYSTEM (FIXED)
# ============================

from patient import Patient
from doctor import Doctor
from appointment import Appointment
from exceptions import DoctorNotFoundError, PatientNotFoundError, AppointmentConflictError

class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    # -------------------------
    # Add / Get Patient & Doctor
    # -------------------------
    def add_patient(self, name, age, phone):
        patient = Patient(name, age, phone)
        self.patients[patient.id] = patient
        print(f"✅ Patient Added Successfully! Patient ID: {patient.id}")
        return patient

    def add_doctor(self, name, specialization):
        doctor = Doctor(name, specialization)
        self.doctors[doctor.id] = doctor
        print(f"✅ Doctor Added Successfully! Doctor ID: {doctor.id}")
        return doctor

    def get_patient(self, patient_id):
        if patient_id not in self.patients:
            raise PatientNotFoundError(f"❌ Patient ID {patient_id} Not Found!")
        return self.patients[patient_id]

    def get_doctor(self, doctor_id):
        if doctor_id not in self.doctors:
            raise DoctorNotFoundError(f"❌ Doctor ID {doctor_id} Not Found!")
        return self.doctors[doctor_id]

    # -------------------------
    # BOOK APPOINTMENT (FIXED)
    # -------------------------
    def book_appointment(self, patient_id, doctor_id, date, time):
        patient = self.get_patient(patient_id)
        doctor = self.get_doctor(doctor_id)

        # Check conflict
        for appt in self.appointments:
            if appt.doctor.id == doctor_id and appt.date == date and appt.time == time:
                raise AppointmentConflictError("❌ Doctor already has an appointment at that time!")

        appointment = Appointment(patient, doctor, date, time)
        self.appointments.append(appointment)
        doctor.schedule.append(f"{date} {time}")

        print(f"✅ Appointment Booked Successfully! Appointment ID: {appointment.id}")
        return appointment

    # -------------------------
    # VIEW SCHEDULES
    # -------------------------
    def view_doctor_schedule(self, doctor_id):
        self.get_doctor(doctor_id)
        schedule = [a for a in self.appointments if a.doctor.id == doctor_id]

        if not schedule:
            print("No Appointments Found.")
        else:
            for a in schedule:
                print(a)

    def view_patient_appointments(self, patient_id):
        self.get_patient(patient_id)
        schedule = [a for a in self.appointments if a.patient.id == patient_id]

        if not schedule:
            print("No Appointments Found.")
        else:
            for a in schedule:
                print(a)

    # -------------------------
    # LISTS
    # -------------------------
    def list_all_patients(self):
        for p in self.patients.values():
            print(p)

    def list_all_doctors(self):
        for d in self.doctors.values():
            print(d)

    # -------------------------
    # REPORTS
    # -------------------------
    def generate_doctor_schedule_report(self, doctor_id):
        self.view_doctor_schedule(doctor_id)

    def generate_patient_history_report(self, patient_id):
        self.view_patient_appointments(patient_id)
