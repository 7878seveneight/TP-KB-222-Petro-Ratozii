from student import *
from studentList import *
from utils import *

def main():
    studentList = StudentList()
    file = input("Enter the name of your file: ")
    studentList = Utils.loadFile(file, studentList)
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, S save,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created")
                student = Student(input("Enter name: "), input("Enter phone: "), input("Enter profession: "), input("Enter group number: "))
                studentList.addStudent(student)
            case "U" | "u":
                print("Existing element will be updated")
                name = input("Enter student name to be updated: ")
                newStudent = Student(input("Enter new name: "), input("Enter new phone: "), input("Enter new age: "), input("Enter new email: "))
                studentList.updateStudent(name, newStudent)
            case "D" | "d":
                print("Element will be deleted")
                name = input("Enter student name: ")
                studentList.deleteStudent(name)
            case "P" | "p":
                print("List will be printed")
                print(studentList)
            case "S" | "s":
                file = input("Enter CSV file name: ")
                Utils.saveFile(file, studentList)
            case "X" | "x":
                print("Exit")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()