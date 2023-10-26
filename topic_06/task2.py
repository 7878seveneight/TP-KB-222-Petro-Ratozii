students = [{'name': 'Petr', 'grade': 110},
            {'name': 'Petro', 'grade': 65},
            {'name': 'Ihor', 'grade': 100},
            {'name': 'NotPetr', 'grade': 70}]

getName = lambda student: student['name']
getGrade = lambda student: int(student['grade'])

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

sorted_by_name = sorted(students, key=getName, reverse=sortType)
print("\n Сортування за ім'ям:")
for student in sorted_by_name:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

sorted_by_grade = sorted(students, key=getGrade, reverse=sortType)
print("\n Сортування за оцінкою:")
for student in sorted_by_grade:
    print(f"Name: {student['name']}, Grade: {student['grade']}")