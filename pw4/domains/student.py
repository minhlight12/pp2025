from domains.person import Person
class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self._dob = dob
        self._gpa = 0.0
    def set_dob(self, dob):
        self._dob = dob
    def set_gpa(self, gpa):
        self._gpa = gpa
    def get_dob(self):
        return self._dob
    def get_gpa(self):
        return self._gpa
    def display(self):  #override => polymorphism
        print(f"{self._id} | {self._name} | {self._dob} | GPA: {self._gpa:.2f}")