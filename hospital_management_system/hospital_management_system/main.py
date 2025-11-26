# ------------------------------------------------------
#                HOSPITAL MANAGEMENT SYSTEM
# ------------------------------------------------------

from hospital_system import HospitalSystem

def main():
    system = HospitalSystem()

    while True:
        print("\n=================================================")
        print("             HOSPITAL MANAGEMENT MENU            ")
        print("=================================================")
        print(" 1. Add Patient")
        print(" 2. Add Doctor")
        print(" 3. Book Appointment")
        print(" 4. View Doctor Schedule")
        print(" 5. View Patient Appointments")
        print(" 6. List All Patients")
        print(" 7. List All Doctors")
        print(" 8. Generate Doctor Schedule Report")
        print(" 9. Generate Patient History Report")
        print("10. Exit")
        print("=================================================")

        choice = input("Enter your choice (1-10): ")

        # ------------------------------------------------------
        # 1. ADD PATIENT
        # ------------------------------------------------------
        if choice == "1":
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            phone = input("Enter patient phone number: ")
            system.add_patient(name, age, phone)

        # ------------------------------------------------------
        # 2. ADD DOCTOR
        # ------------------------------------------------------
        elif choice == "2":
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            system.add_doctor(name, specialization)

        # ------------------------------------------------------
        # 3. BOOK APPOINTMENT
        # ------------------------------------------------------
        elif choice == "3":
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date (DD-MM-YYYY): ")
            time = input("Enter appointment time (e.g., 10:30 AM): ")
            system.book_appointment(patient_id, doctor_id, date, time)

        # ------------------------------------------------------
        # 4. VIEW DOCTOR SCHEDULE
        # ------------------------------------------------------
        elif choice == "4":
            doctor_id = input("Enter doctor ID: ")
            system.view_doctor_schedule(doctor_id)

        # ------------------------------------------------------
        # 5. VIEW PATIENT APPOINTMENTS
        # ------------------------------------------------------
        elif choice == "5":
            patient_id = input("Enter patient ID: ")
            system.view_patient_appointments(patient_id)

        # ------------------------------------------------------
        # 6. LIST ALL PATIENTS
        # ------------------------------------------------------
        elif choice == "6":
            system.list_all_patients()

        # ------------------------------------------------------
        # 7. LIST ALL DOCTORS
        # ------------------------------------------------------
        elif choice == "7":
            system.list_all_doctors()

        # ------------------------------------------------------
        # 8. DOCTOR SCHEDULE REPORT
        # ------------------------------------------------------
        elif choice == "8":
            doctor_id = input("Enter doctor ID: ")
            system.generate_doctor_schedule_report(doctor_id)

        # ------------------------------------------------------
        # 9. PATIENT HISTORY REPORT
        # ------------------------------------------------------
        elif choice == "9":
            patient_id = input("Enter patient ID: ")
            system.generate_patient_history_report(patient_id)

        # ------------------------------------------------------
        # 10. EXIT
        # ------------------------------------------------------
        elif choice == "10":
            print("✅  Thank You!")
            break

        # ------------------------------------------------------
        # INVALID CHOICE
        # ------------------------------------------------------
        else:
            print("⚠️ Invalid choice! Please select between 1-10.")

if __name__ == "__main__":
    main()

