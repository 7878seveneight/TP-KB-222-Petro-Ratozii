import unittest
from unittest.mock import patch
from io import StringIO
from main import main
import os
from utils import Utils
from studentList import *
from student import *

class Tests(unittest.TestCase):
    def test_Student(self):
        student = Student("Bobb", "061234567", "CS", "221")
        self.assertEqual(student.name, "Bobb")
        self.assertEqual(student.phone, "061234567")
        self.assertEqual(student.profession, "CS")
        self.assertEqual(student.groupNum, "221")

    def setUp(self):
        self.studentList = StudentList()
        self.student1 = Student("Bob", "061234567", "CS", "221")
        self.student2 = Student("Zak", "061234567", "PE", "223")

    def test_addStudent(self):
        self.studentList.addStudent(self.student1)
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Bob")

        self.studentList.addStudent(self.student2)
        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[1].name, "Zak")

    def test_deleteStudent(self):
        self.studentList.addStudent(self.student1)
        self.studentList.addStudent(self.student2)

        self.studentList.deleteStudent("Bob")
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Zak")

        self.studentList.deleteStudent("John")
        self.assertEqual(len(self.studentList.students), 1)

    def test_updateStudent(self):
        self.studentList.addStudent(self.student1)
        self.studentList.addStudent(self.student2)

        newStudent = Student("Bob", "061234567", "CS", "221")
        self.studentList.updateStudent("Bob", newStudent)

        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[0].phone, "061234567")
        self.assertEqual(self.studentList.students[0].groupNum, "221")

        nonExistingStudent = Student("John", "061234567", "CS", "223")
        self.studentList.updateStudent("John", nonExistingStudent)

        self.assertEqual(len(self.studentList.students), 2)

    def test_loadFile(self):
        self.testFile = "unittests.csv"
        self.studentList = StudentList()
        with open(self.testFile, "w") as file:
            file.write("name,phone,profession,groupNum\nBobb,061234567,CS,221")
        Utils.loadFile(self.testFile, self.studentList)
        self.assertEqual(len(self.studentList.students), 1)

    def test_saveFile(self):
        self.testFile = "unittests.csv"
        self.studentList = StudentList()
        student = Student("Bobb", "061234567", "CS", "221")
        self.studentList.addStudent(student)
        Utils.saveFile(self.testFile, self.studentList)
        self.assertTrue(os.path.exists(self.testFile))


if __name__ == '__main__':
    unittest.main()