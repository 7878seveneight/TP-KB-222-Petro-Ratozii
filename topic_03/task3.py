dict1 = {'a': 1, 'b': 2}
dict1.update({'c': 3, 'd': 4})
print(f"Update example result: {dict1} \n\tUpdating(adding) dictionary with new elements")

dict2 = {'a': 1, 'b': 2, 'c': 3}
del dict2['b']
print(f"del(Delete) example result: {dict2} \n\tDeletes an element from the dictionary")

dict3 = {'a': 1, 'b': 2}
dict3.clear()
print(f"Clear example result: {dict3} \n\tJust clears the dictionary")

dict4 = {'a': 1, 'b': 2, 'c': 3}
keys = dict4.keys()
print(f"Keys example result: {keys} \n\tShows keys from the dictionary")

dict5 = {'a': 1, 'b': 2, 'c': 3}
values = dict5.values()
print(f"Values example result: {values} \n\tShows values from the dictionary")

dict6 = {'a': 1, 'b': 2, 'c': 3}
items = dict6.items()
print(f"Items example result: {items} \n\tShows items(list of tuples containing key-value pairs in the dictionary*) from the dictionary")