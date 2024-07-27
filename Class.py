class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name=name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def __str__(self):
        return f"Name: {self.name}, Major: {self.major}, GPA: {self.gpa}, Probation: {self.is_on_probation}"
