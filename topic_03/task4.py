def findInsertPosition(sorted_list, newElem):
    position = 0
    for i in sorted_list:
        if newElem < i:
            break
        position += 1
    return position

list = ["aa", "ee", "zz"]
newElem = input("Your new element: ")

insert_position = findInsertPosition(list, newElem)
list.insert(insert_position, newElem)

print(f"Position: {insert_position} \nUpdated list: {list}")