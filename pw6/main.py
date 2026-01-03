from domains.school_manager import SchoolManager 
from input import get_choice
from output import show_menu
from storage import save_students, save_marks, save_courses, save_data, load_data
import os
def main():
    sm = SchoolManager()
    students, courses, marks = load_data()
    if students is not None:
        sm.students = students
        sm.courses = courses
        sm.marks = marks
        print("Loaded data from students.dat")
    else:
        sm.input_students()
        sm.input_courses()
    while True:
        show_menu()
        choice = get_choice()

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
            sm.update_all_gpa()
            save_data(sm.students, sm.courses, sm.marks)
            print("Data saved using pickle")
            break
        else:
            print("Invalid choice")
main()