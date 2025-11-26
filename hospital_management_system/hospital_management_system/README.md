# Hospital Patient Management (Student Copy)

hospital_management/
│── main.py              # Entry point (menu-driven)
│── patient.py           # Patient class
│── doctor.py            # Doctor class
│── appointment.py       # Appointment class
│── hospital_system.py   # Main system logic
│── report.py            # Reporting functions
│── exceptions.py        # Custom exceptions
│── utils.py             # Helper functions (ID generator, validations)
│── README.md            # Instructions for students

 
## Problem Statement
Build a hospital system to manage patients, doctors, and appointments.
 Patients can book appointments with doctors, and the system ensures no
  double-booking.


## Topics Covered
- Classes \& Objects
- Lists \& Dictionaries
- Exception Handling
- Reports \& Summaries
- Modular Programming


## Step-by-Step Workflow
1. Implement Patient class
2. Implement Doctor class
3. Implement Appointment class
4. Implement HospitalSystem (core logic)
5. Add reporting functions
6. Create menu-driven interface in main.py

## Student Breakdown
Student A builds the Patient, Doctor, Appointment classes → shared with Student B.
Student B builds HospitalSystem + exceptions + utils using A’s models → shared with Student C.
Student C integrates with report + main.py to complete the system.

 
