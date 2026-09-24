course_count = int(input("Enter the number of courses:"))
course_information = []
for i in range(course_count):
    course_name = input(f"Enter the name of course {i + 1}:")
    course_id = input(f"Enter the code of course {i + 1}:")
    course_information.append({
        "course_name": course_name,
        "course_id": course_id,
    })

student_count = int(input("Enter the number of students:"))
student_information = []
for i in range(student_count):
    name = input(f"Enter the name of student {i + 1}:")
    id_number = input(f"Enter the ID number of student {i + 1}:")
    date_of_birth = input(f"Enter the date of birth of student {i + 1} (YYYY-MM-DD):")
    student_information.append({
        "name": name,
        "id_number": id_number,
        "date_of_birth": date_of_birth
    })

for course in course_information:
    print(f"Course Name: {course['course_name']}, Course ID: {course['course_id']}")
for student in student_information:
    print(f"Student Name: {student['name']}, ID Number: {student['id_number']}, Date of Birth: {student['date_of_birth']}")

mark = float(input("Enter the student's mark in this course: "))
mark_information = {
    "course_name": course['course_name'],
    "student_name": student['name'],
    "mark": mark
}
for course in course_information:
    if course['course_name'] == mark_information['course_name']:
        print(f"Mark for {mark_information['student_name']} in {mark_information['course_name']}: {mark_information['mark']}")
