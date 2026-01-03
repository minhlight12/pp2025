from domains.school_manager import SchoolManager 
from input import get_choice
from output import show_menu
from storage import save_students, save_marks, save_courses, compress_data, decompress_data
import os
def main():
    if os.path.exists("students.dat"):
        print("Found students.dat -> decompressing...")
        decompress_data()

    sm = SchoolManager()
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
            save_students(sm.students)
            save_courses(sm.courses)
            save_marks(sm.marks)
            compress_data()
            print("Saved and compressed")
            break
        else:
            print("Invalid choice")
main()