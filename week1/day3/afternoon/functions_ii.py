x = [
    [5, 2, 3],
    [10, 8, 9]
]

z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# print(x)
# print(x[1])
# print(
#   x[1][0] # 10
# )
# x[1][0] = 15
# print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
# print(students)
# print(students[0])
# print(students[0]['last_name'])
# students[0]['last_name'] = 'Bryant'
# print(students)

# In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# print(sports_directory['soccer'][0])
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# Change the value 20 in z to 30
# z = [{'x': 10, 'y': 20}]
# z[0]['y'] = 30
# print(z)

# **************************************
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_listt):
    # print(some_listt)
    # loop to print out all the items in the list
    for some_item in some_listt:
        # print(some_item)
        print(f"first_name - {some_item['first_name']}, last_name - {some_item['last_name']}")


iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
