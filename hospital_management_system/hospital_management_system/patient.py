# ============================
#        PATIENT CLASS
# ============================

from utils import generate_id

class Patient:
    def __init__(self, name, age, phone):
        self.id = generate_id("PAT")  # Auto-generate like PAT123
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"{self.id} - {self.name} | Age: {self.age} | Phone: {self.phone}"
