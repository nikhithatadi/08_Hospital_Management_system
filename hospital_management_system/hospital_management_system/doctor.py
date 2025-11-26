# ============================
#         DOCTOR CLASS
# ============================

from utils import generate_id

class Doctor: 
    def __init__(self, name, specialization):
        self.id = generate_id("DOC")    
        self.name = name
        self.specialization = specialization
        self.schedule = []   

    def __str__(self):
        return f"{self.id} | Name: {self.name} | Specialization: {self.specialization}"
