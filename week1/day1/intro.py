# Python

# [x] Virtual Environment
# [x] Version
# [x] Print
print('Hello, World!')
# [x] Data Types
# [x] Primitive
# strings
var_name = 'Ace'
# integers
some_int = 1
# floats
some_float = 1.1
# boolean
some_boolean = False
# [x] Composite
var_tuple = (1, 'name')  # immutable
#            0    1      2
var_list = [123, 2313, 'sdfdsf']  # arrays
# print(var_list[1])
# print(len(var_list))
print(type(var_tuple))
var_dictionary = {
    'key_name': 'value',
    'students': ['Kyle', 'Zach'],
    'student': {
        'first_name': 'Thomas',
        'hobby': 'Dragon Ball Z'
    },
}  # object
# print(var_dictionary['student']['hobby'])
# [x] Conditionals
age = 21
if age < 21:
    print("Can't drink yet")
    # print('Can\'t drink yet')
elif age >= 21:
    print("See you at happy hour!")
else:
    print('Something went wrong')


# [x] Loops
#             start, stop, step
# for i in range(101):
# for (var i = 0; i < 101; i++){}
# for i in range(0, 101, 2):
#   print(i)
cond = True
# while cond:
#   print('It\'s True!')

# [x] Functions


def make_pbj():
    # do some stuff
    print('Function called!')
    print('Make some PBJ🥜🧈🍩')


# make_pbj()
# make_pbj()
# make_pbj()

# [x] Default Parameters & Named Arguments

def make_sandwhich(name, ingredients=[]):
    # do some stuff
    print('Function called!')
    # print('Make some ' + name)
    print(f'Make some {name}')
    # loop over ingredients
    print('The ingredients are:')
    for single_ingredient in ingredients:
        print(single_ingredient)

# make_sandwhich(
#   'Monte Cristo',
#   ['ham', 'jelly', 'pickles', 'eggs', 'bread']
# )

# make_sandwhich('BLT')


def some_name():
    pass
    # what am I suppose to do?
