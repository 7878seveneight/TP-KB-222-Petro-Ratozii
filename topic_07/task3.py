class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Petr", 19),
    Student("Petro", 20),
    Student("Ihor", 27),
    Student("NotPetr", 18),
    Student("Ivan", 17),
]

while True:
    whichSort = input("Sort by descending or ascending: ")
    if whichSort == "ascending":
        sortType = True
        break
    elif whichSort == "descending":
        sortType = False
        break
    else: 
        print("Invalid option. Try againg...")

sortStudents = sorted(students, key=lambda student: student.age, reverse=sortType)
for student in sortStudents:
    print(f"Name: {student.name}, Age: {student.age}")