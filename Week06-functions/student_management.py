# program to manage students
# Author: Carmine Giardino


def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice


students = []


def read_modules():
    modules = []
    module_name = input("\tEnter the module name: ").strip()
    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\tEnter grade: "))
        modules.append(module)
        module_name = input("\tEnter the next module name: ").strip()
    return modules


def do_add(students):
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()
    students.append(current_student)


def do_view(students):
    for student in students:
        print(student["name"])
        display_modules(student["modules"])


def display_modules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{module['name']} \t{module['grade']}")


def do_nothing():
    pass


choice_map = {"a": do_add, "v": do_view, "q": do_nothing()}

choice = display_menu()
while choice != "q":
    if choice in choice_map:
        # running choice using a map
        choice_map[choice](students)
    elif choice != "q":
        print("\n\nplease select either a,v or q")
    choice = display_menu()
