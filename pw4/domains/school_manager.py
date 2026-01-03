import math
import numpy as np
from domains.student import Student 
from domains.course import Course
class SchoolManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
    # STUDENTS
    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"#Student {i+1}")
            id = int(input("Enter student id: "))
            name = input("Enter student name: ")
            dob = input("Enter date of birth: ")
            self.students.append(Student(id, name, dob))
    #COURSES
    def input_courses(self):
        m = int(input("Enter number of courses: "))
        for i in range(m):
            print(f"#Courses {i+1}")
            id = int(input("Enter course id: "))
            name = input("Enter course name: ")
            credits = int(input("Enter credits of course: "))
            self.courses.append(Course(id, name, credits))
        
        for i in range(len(self.students)):
            row = []
            for j in range(len(self.courses)):
                row.append(0)
            self.marks.append(row)

    def list_student(self):
        print("\nList of students:")
        for s in self.students:
            s.display()

    def list_courses(self):
        print("\nList of courses:")
        for c in self.courses:
            c.display()

    def input_marks(self):
        index = int(input("Select course index: ")) - 1
        if index < 0 or index >= len(self.courses):
            print("Invalid course index")
            return
        for i in range(len(self.students)):
            mark = float(input(f"Enter mark for {self.students[i].get_name()}: "))
            self.marks[i][index] = mark
    
    def show_marks(self):
        index = int(input("Select course index: ")) - 1  #the position of subject in courses
        if index < 0 or index >= len(self.courses):
           print("Invalid course index")
           return
        print(f"\nMarks for course {self.courses[index].get_name()}")
        for i in range(len(self.students)):
           print(f"\n{self.students[i].get_name()} : {self.marks[i][index]}")

    def round_down(self):
        index = int(input("Select course index: ")) - 1  #the position of subject in courses
        print(f"After rounding-down, Marks for course {self.courses[index].get_name()}")
        for i in range(len(self.students)):
            print(f"\n{self.students[i].get_name()} : {math.floor(self.marks[i][index] * 10) / 10}")

    def cal_avrGPA_each_student(self, student_index):
        marks = self.marks[student_index]
        credits = [c.get_credits() for c in self.courses]
        marks_arr = np.array(marks)
        credits_arr = np.array(credits)
        gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        return gpa
    
    def update_all_gpa(self):
        for i in range(len(self.students)):
            gpa = self.cal_avrGPA_each_student(i)
            self.students[i].set_gpa(gpa) 
    
    def comparegpa(self, student):
        return student.get_gpa()
    
    def sort_students_by_gpa(self):
        self.update_all_gpa()
        self.students.sort(key=self.comparegpa,reverse=True)