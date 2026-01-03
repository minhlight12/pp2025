class Course:
    def __init__(self,id,name,credits):
        self._id = id
        self._name = name
        self._credits = credits
    def set_id(self, id):
        self._id = id
    def set_name(self, name):
        self._name = name
    def set_credits(self, credits):
        self._credits = credits
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_credits(self):
        return self._credits
    def display(self):
        print(f"{self._id} | {self._name} | {self._credits}")