class Student():
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade


    def __str__(self):
        return f"Student's name: {self.name} \nStudent's age: {self.age} \nStudent's grade: {self.grade}"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Student's age must be greater than 0.")
        self._age = age

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        if grade < 0:
            raise ValueError("Student's grade must be greater than 0.")
        self._grade = grade

def getStudent():
    try:
        name = input("Student's name: ")
        age = int(input("Student's age: "))
        grade = int(input("Student's grade: "))
        student = Student(name, age, grade)
    except Exception as e:
        print(e)
        return getStudent()
    else:
        return student

def main():
    amount = int(input('Amount of your students: '))
    students = []

    for _ in range(amount):
        students.append(getStudent())
        print("\n")

    for student in sorted(students, key=lambda s: s.grade):
        print(f"\n{student}")

main()