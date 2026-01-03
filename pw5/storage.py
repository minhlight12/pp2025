import zipfile
import os
from domains.student import Student
from domains.course import Course
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

def compress_data():
    with zipfile.ZipFile("students.dat", "w") as z:
        if os.path.exists("students.txt"):
            z.write("students.txt")
        if os.path.exists("courses.txt"):
            z.write("courses.txt")
        if os.path.exists("marks.txt"):
            z.write("marks.txt")

def decompress_data():
    with zipfile.ZipFile("students.dat", "r") as z:
        z.extractall()