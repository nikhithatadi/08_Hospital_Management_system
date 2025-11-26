# ============================
#   CUSTOM EXCEPTIONS
# ============================

class DoctorNotFoundError(Exception):
    """Raised when a doctor ID is not found in the system."""
    pass

class PatientNotFoundError(Exception):
    """Raised when a patient ID is not found in the system."""
    pass

class AppointmentConflictError(Exception):
    """Raised when the requested appointment time conflicts with doctor's schedule."""
    pass
