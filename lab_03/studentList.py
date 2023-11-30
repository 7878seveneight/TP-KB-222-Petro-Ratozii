from student import *

class StudentList():
    def __init__(self) -> None:
        self.students = []

    def __str__(self) -> str:
        string = ""
        for student in self.students:
            string += f"name {student.name}, phone {student.phone}, profession {student.profession}, groupNum {student.groupNum}\n"
        return string
    
    def addStudent(self, student: Student):
        insertPosition = 0
        for item in self.students:
            if student.name > item.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student)
        print("New element has been added")
    
    def deleteStudent(self, studentName):
        deletePosition = -1
        for student in self.students:
            if student.name == studentName:
                deletePosition = self.students.index(student)
                break
        if deletePosition == -1:
            print("Element not found")
        else:
            print("Delete position " + str(deletePosition))
            del self.students[deletePosition]
    
    def updateStudent(self, studentName, newStudent: Student):
        updatePosition = -1 
        for student in self.students:
            if studentName == student.name:
                updatePosition = self.students.index(student)
                break
        if updatePosition == -1:
            print("Element was not found")
            return
        
        if studentName != newStudent.name:
            del self.students[updatePosition]
            self.addStudent(newStudent)
        else:
            self.students[updatePosition].phone = newStudent.phone
            del newStudent