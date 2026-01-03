import math
import numpy as np
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

def main():
    sm = SchoolManager()
    sm.input_students()
    sm.input_courses()
    while True:
        print("\n --MENU--")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Round-down student scores to 1-degit decimal")
        print("5. Show marks for a course")
        print("6. Sort student list by GPA descending")
        print("0. Exit")

        choice = input("Choice: ")
        if(choice == '1'):
            sm.list_student()
        elif(choice == '2'):
            sm.list_courses()
        elif(choice == '3'):
            sm.input_marks()
        elif(choice == '4'):
            sm.round_down()
        elif(choice == '5'):
            sm.round_down()
            sm.show_marks()
        elif(choice == '6'):
            sm.sort_students_by_gpa()
            sm.list_student()
        elif(choice == '0'):
            break
        else:
            print("Invalid choice")
main()