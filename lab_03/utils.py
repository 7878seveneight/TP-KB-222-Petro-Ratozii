from student import *
from studentList import *
import csv

class Utils:
    @staticmethod
    def loadFile(file, studentList):
        with open(file, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                student = Student(row["name"], row["phone"], row["profession"], row["groupNum"])
                studentList.addStudent(student)
        return studentList

    @staticmethod
    def saveFile(file, studentList):
            with open(file, 'w', newline="") as SaveFile:
                fieldnames = ["name", "phone", "profession", "groupNum"]
                writer = csv.DictWriter(SaveFile, fieldnames=fieldnames)
                writer.writeheader()
                for student in studentList.students:
                    writer.writerow({"name": student.name, "phone": student.phone, "profession": student.profession, "groupNum": student.groupNum})
                print("File is saved.")