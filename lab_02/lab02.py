import csv
import sys

def loadFile(fileName):
    list = []
    with open(fileName) as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({"name": row["name"], "phone": row["phone"], "profession": row["profession"], "groupNum": row["groupNum"]})
    return list

def saveFile(fileName, list):
    fieldnames = ["name", "phone", "profession", "groupNum"]

    with open(fileName, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)

def printAllList(list):
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Profession is " + elem["profession"] + ", Group number is " + elem["groupNum"]
        print(strForPrint)
    return

def addNewElement(list):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    profession = input("Please enter student profession: ")
    groupNum = input("Please enter student group number: ")
    newItem = {"name": name, "phone": phone, "profession": profession, "groupNum": groupNum}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement(list):
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement(list):
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    trueForDel = False
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        print("Update position " + str(updatePosition))
        trueForDel = True

    if trueForDel == True:
        del list[updatePosition]
    
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    profession = input("Please enter student profession: ")
    groupNum = input("Please enter student group number: ")
    newItem = {"name": name, "phone": phone, "profession": profession, "groupNum": groupNum}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("The element has been updated.")
    return

def main():
    if len(sys.argv) != 2:
        print("\tUse \"python lab02 lab2.csv\"")
        sys.exit(1)
    fileName = sys.argv[1]
    list = loadFile(fileName)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, S save,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(list)
                printAllList(list)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(list)
                printAllList(list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(list)
            case "P" | "p":
                print("List will be printed")
                printAllList(list)
            case "S" | "s":
                print("File is saved")
                saveFile(fileName, list)
            case "X" | "x":
                print("Exit")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()