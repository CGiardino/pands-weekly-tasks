# Write a program that stores a student name and list of her courses and 
# grades in a dict, the program should then print out her data.
# Author: Carmine Giardino

students = []
while True:
    student_name = input("Enter student name: ")
    if student_name == "":
        break
    modules = []
    while True:
        course_name = input("Enter course name: ")
        if course_name == "":
            break
        while True:
            try:
                course_grade = int(input("Enter course grade: "))
                break
            except ValueError:
                print("Grade must be a number")
        modules.append({"courseName": course_name, "grade": course_grade})
    student = {
        "name": student_name,
        "modules": modules
    }
    students.append(student)
for student in students:
    print("Student: {}".format(student["name"]))
    for module in student["modules"]:
        print("\t {} \t: {}".format(module["courseName"], module["grade"]))
