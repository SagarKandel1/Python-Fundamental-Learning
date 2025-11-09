from random import choice
#arry where we store the student data
students = []

def print_welcome_message():
    print("===========================================================")
    print('Welcome to the Python Student Management System Menu')
    print("===========================================================\n")


# Function to add a new student
def add_student():
    print("Add New Student")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    student_id = input("Enter Student ID: ")

    # How we store the Student details as a dictionary
    student = {
        "name": name,
        "age": age,
        "id": student_id

    }
    # Adding students to a list
    students.append(student)
    print(f"Studnet '{name}' add successfully")


# Function to View students
def view_student():
    print("\n View Student List")
    if not students:
        print("No Students found.\n")
        return
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, Age: {student['age']}, ID: {student['id']}")
    print()

def update_student():
    print("Update Student")
    student_id = input("Enter Student ID")

    for std in students:
        if std['id'] == student_id:
            print(f"Edit details for {std['name']}")
            std['name'] = input("Enter new name")
            std['age'] = input("Enter new age")
            print("Upadated details for {name}")
            return
    print("Details not found.\n")


if __name__ == '__main__':
    print_welcome_message()

while True:
    print("1. Add New Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Exit")

    user_option = input()
    if user_option == '1':
       add_student()
    elif user_option == '2':
        view_student()
    elif user_option == '3':
        view_student()
    elif user_option == '4':
        print("Exit")
        break
    else:
        print("Invalid option. Please try again.\n")




