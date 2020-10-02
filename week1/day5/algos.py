# /*
#   Zip Arrays into Map


#   Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.

#   Associative arrays are sometimes called maps because a key (string) maps to a value
#  */

keys1 = ["abc", 3, "yo"]
vals1 = [42, "wassup", True]
expected1 = {
    'yo': True,
    'abc': 42,
    '3': "wassup",
}


def zipArraysIntoMap(keys, values):
    # create a dictionary
    dictionary = {}
    # loop through both lists
    for index in range(0, len(keys)):
        print(index)
        print(keys[index], values[index])
        key = keys[index]
        value = values[index]
        dictionary[key] = value
        # create new key value pair in dictionary
        # return the dictionary
    print(dictionary)
    return dictionary


# zipArraysIntoMap(keys1, vals1)
# /* ******************************************************************************** */

# /*
#   Invert Hash

#   A hash table / hash map is an obj / dictionary

#   Given an object / dict,
#   return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
# */

obj1 = {'name': "Zaphod", 'charm': "high", 'morals': "dicey"}
expected1 = {'Zaphod': "name", 'high': "charm", 'dicey': "morals"}


def invertObj(obj):
    # create a dictionary
    dictionary = {}
    # loop through objects
    for original_key, original_value in obj.items():
        # create our new key value
        # print(key, obj[key])
        print(original_key, original_value)
        new_value = original_key
        new_key = original_value
        dictionary[new_key] = new_value
    print(dictionary)
    return dictionary


invertObj(obj1)

# PascalCase
# camelCase
# snake_case
