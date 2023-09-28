list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"Extend example result: {list1} \n\tExtending list1 with another list (list2)")

list3 = [1, 2, 3]
list3.append(4)
print(f"Append example result: {list3} \n\tAdding another element to the list")

list4 = [1, 2, 3]
list4.insert(1, 4)
print(f"Insert example result: {list4} \n\tAdding two elements to the list")

list5 = [1, 2, 3, 2]
list5.remove(2)
print(f"Remove example result: {list5} \n\tRemoves one element from the list")

list6 = [1, 2, 3]
list6.clear()
print(f"Clear example result: {list6} \n\tJust clears the list")

list7 = [3, 1, 2]
list7.sort()
print(f"Sort example result: {list7} \n\tSorting the list")

list8 = [1, 2, 3]
list8.reverse()
print(f"Reverse example result: {list8} \n\tReversing the list backwards")

list9 = [1, 2, 3]
copy_of_list9 = list9.copy()
print(f"Copy example: {copy_of_list9} \n\tCopies one list to another")

print("\n\n")
# other
list10 = [1, 2, 3]
list10 += [4, 5, 6]
print(f"Adding elements to the list. Works like extend, but you don't have to add new lists. {list10}")

list11 = [1, 2, 3]
list11 += [4]
print(f"Works like append: {list11}")

list12 = [1, 2, 3]
list12[1:1] = [4]
print(f"Works like insert, but you can manage position of the new element {list12}")

list13 = [1, 2, 3, 2]
while 2 in list13:
    index = list13.index(2)
    list13 = list13[:index] + list13[index+1:]
print(f"Deletes sertain elements in the list (2 in example) {list13}")