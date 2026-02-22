class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


def save_student(student):
    with open("data.txt", "a") as file:
        file.write(student.id + "," + student.name + "," + student.age + "\n")


def view_students():
    with open("data.txt", "r") as file:
        data = file.readlines()
        for line in data:
            print(line)


def delete_student(students):
    id = input("Enter ID to delete: ")
    new_data = []

    with open("data.txt", "r") as file:
        data = file.readlines()

    for line in data:
        if not line.startswith(id):
            new_data.append(line)

    with open("data.txt", "w") as file:
        for line in new_data:
            file.write(line)

    print("Record Deleted")