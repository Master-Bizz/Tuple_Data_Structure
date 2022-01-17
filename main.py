print('meh')
# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Elements can be of different data types

'''
Creating a Tuple
'''

# Empty tuple
tuple = ()
# tuple can hold heterogeneous (different) data types
tuple = ("cat", [4, 3, 2], (1, 2, 3))
tuple = 'yo ,'
print(tuple)
tuple = 'yoo'
print(tuple)

'''
Access Tuple Elements
'''
tuple = (1234, 4321, 'hello!')
print(tuple[1])

'''
Negative Indexing
'''
print(tuple[-1])
print(tuple[-2])

'''
Slicing Tuples in Python
'''

fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
print(fruits[2:3])
print(fruits[1:-1])
print(fruits[2:])
print(fruits[:3])
print(fruits[-2:])
print(fruits[2:2:])
print(fruits[:2:])

'''
Changing a Tuple
'''
random = ("cat", [4, 3, 2])
# random[0] = "cherry"  # comes up with an Error as its immutable: Once a Tuple is set, it cannot be changed.
random[1][2] = [89]
print(random)   # List data types are always mutable though.

'''
Deleting a Tuple
'''
# del fruits - alwayas works but not for indivitual items.

'''
Tuple Methods
'''
print(dir(list))
print(dir(tuple))

print(random.index('cat'))
print(random.count('cat'))
print(len('cat'))
print(str('cat'))
