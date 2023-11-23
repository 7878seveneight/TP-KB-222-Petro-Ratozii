import unittest
from unittest.mock import patch
from lab02 import *
import io
import os
import csv

class Lab2Test(unittest.TestCase):
    def setUp(self):
        self.testFile = "testData.csv"
        self.testData = [
            {"name": "Bob", "phone": "061234567", "profession": "CS", "groupNum": "222"},
            {"name": "Emma", "phone": "061234568", "profession": "PE", "groupNum": "221"}
        ]

    def tearDown(self):
        if os.path.exists(self.testFile):
            os.remove(self.testFile)
    
    def test_loadFile(self):
        with open(self.testFile, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "profession", "groupNum"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.testData)

        updatedList = loadFile(self.testFile)
        self.assertEqual(updatedList, self.testData)

    def test_saveFile(self):
        studentList = self.testData
        saveFile(self.testFile, studentList)
        self.assertTrue(os.path.exists(self.testFile))

    def test_printAllList(self):
        studentList = self.testData
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(studentList)
            output = mock_stdout.getvalue()
            self.assertIn("Bob", output)
            self.assertIn("Emma", output)

    def test_addNewElement(self):
        studentList = self.testData
        with patch('builtins.input', side_effect=["New Student", "061234567", "CS", "223"]):
            addNewElement(studentList)
            self.assertEqual(len(studentList), 3)

    def test_deleteElement(self):
        studentList = self.testData
        with patch('builtins.input', return_value="Bob"):
            deleteElement(studentList)
            self.assertEqual(len(studentList), 1)

    def test_updateElement(self):
        studentList = self.testData
        with patch('builtins.input', side_effect=["Bob", "Emma", "061234567", "CS", "223"]):
            updateElement(studentList)
            self.assertEqual(studentList[0]["name"], "Emma")

if __name__ == '__main__':
    unittest.main()