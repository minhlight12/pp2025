import zipfile
import os
import pickle
from domains.student import Student
from domains.course import Course
temp_pickle = "data.pkl"
zip_file = "students.dat"
def save_students(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()},{s.get_gpa()}\n")

def save_courses(courses):
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

def save_marks(marks):
    with open("marks.txt", "w") as f:
        for row in marks:
            for m in row:
                f.write(str(m) + ",")
            f.write("\n")

def save_data(students, courses, marks):
    with open(temp_pickle, "wb") as f:
        pickle.dump({"students": students, "courses": courses, "marks": marks},f)
    with zipfile.ZipFile(zip_file, "w") as z:
        z.write(temp_pickle)
    os.remove(temp_pickle)

def load_data():
    if not os.path.exists(zip_file):
        return None, None, None
    
    #decompress
    with zipfile.ZipFile("students.dat", "r") as z:
        z.extractall()

    #unpickle
    with open(temp_pickle, "rb") as f:
        data = pickle.load(f)
    
    #delete temporary pickle file 
    os.remove(temp_pickle)

    return data["students"], data["courses"], data["marks"]