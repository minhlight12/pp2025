def input_num_students():
    return int(input("Enter number of students:" ))

def input_student(n):
    students = []
    for i in range(n):
        print(f"#Student {i+1}")
        id = int(input("Enter student id: "))
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")
        students.append([id,name,dob])
    return students

def input_num_courses():
    return int(input("Enter number of courses: "))

def input_courses(m):
    courses = []
    for i in range(m):
        print(f"#Courses {i+1}")
        id = (input("Enter course id: "))
        name = input("Enter course name: ")
        courses.append([id,name])
    return courses

def list_student(students):
    print("\nList of students:")
    for s in students:
        print(f"\n{s[0]} | {s[1]} | {s[2]} ")

def list_courses(courses):
    print("\nList of courses:")
    for c in courses:
        print(f"\n{c[0]} | {c[1]}")

def input_marks(students, courses, marks):
    index = int(input("Select course index: ")) #the position of subject in courses
    if index < 0 or index >= len(courses):
        print("Invalid course index")
        return
    for i in range(len(students)):
        mark = float(input(f"Enter mark for {students[i][1]}: "))
        marks[i][index] = mark

def show_marks(students, courses, marks):
    index = int(input("Select course index: ")) #the position of subject in courses
    if index < 0 or index >= len(courses):
        print("Invalid course index")
        return
    print(f"\nMarks for course {courses[index][1]}")
    for i in range(len(students)):
        print(f"\n{students[i][1]} : {marks[i][index]}")

def main():
    n = input_num_students()
    students = input_student(n)

    m = input_num_courses()
    courses = input_courses(m)

    marks = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        marks.append(row)

    while True:
        print("\n --MENU--")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show marks for a course")
        print("0. Exit")

        choice = input("Choice: ")
        if(choice == '1'):
            list_student(students)
        elif(choice == '2'):
            list_courses(courses)
        elif(choice == '3'):
            input_marks(students, courses, marks)
        elif(choice == '4'):
            show_marks(students, courses, marks)
        elif(choice == '0'):
            break
        else:
            print("Invalid choice")
main()
