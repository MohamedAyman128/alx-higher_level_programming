#!/usr/bin/python3
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
a = a_dictionary.values()
s = sorted(a)
print(a)
print(s)
print(s[-1])
print('======================')
n = sorted(a_dictionary.items(), key=lambda x: x[1])

print(n)
print(n[-1][0])
print('======================')
m = sorted(a_dictionary)
print(a_dictionary.items())
print(m)
