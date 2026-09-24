students = []
courses = []
marks = []

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    students.append({
        "name": name,
        "id": student_id,
        "dob": date_of_birth
    })

def add_course():
    course_name = input("Enter course name: ")
    course_id = input("Enter course ID: ")
    courses.append({
        "name": course_name,
        "id": course_id
    })

def add_mark():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    mark = float(input("Enter mark: "))
    marks.append({
        "student_id": student_id,
        "course_id": course_id,
        "mark": mark
    })

def display_students():
    for student in students:
        print(f"Name: {student['name']}, ID: {student['id']}, DOB: {student['dob']}")

def display_courses():
    for course in courses:
        print(f"Course Name: {course['name']}, Course ID: {course['id']}")

def display_marks():
    for mark in marks:
        student = next((s for s in students if s['id'] == mark['student_id']), None)
        course = next((c for c in courses if c['id'] == mark['course_id']), None)
        if student and course:
            print(f"Student: {student['name']}, Course: {course['name']}, Mark: {mark['mark']}")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Mark")
    print("4. Display Students")
    print("5. Display Courses")
    print("6. Display Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        add_course()
    elif choice == '3':
        add_mark()
    elif choice == '4':
        display_students()
    elif choice == '5':
        display_courses()
    elif choice == '6':
        display_marks()
    elif choice == '7':
        break
    else:
        print("Invalid choice, please try again.")
