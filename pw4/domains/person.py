class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def set_id(self, id):
        self._id = id
    def set_name(self, name):
        self._name = name
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def display(self):
        print(f"{self._id} | {self._name} ")