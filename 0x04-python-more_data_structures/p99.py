#!/usr/bin/python3
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
items = a_dictionary.items()
a = a_dictionary.keys()
b  = a_dictionary.values()
new = {key: val*2 for key, val in items }
print(new)
print(sorted(items))
