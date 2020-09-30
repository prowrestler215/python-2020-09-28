# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list_parameter):
    # create our dictionary to add our values
    analysis = {
        'sumTotal': 0,
        'average': 0,
        'minimum': list_parameter[0],
        'maximum': list_parameter[0],
        'length': 0
    }

    # look through the list
    for number in list_parameter:
        # do some math
        analysis['sumTotal'] += number
        if number < analysis['minimum']:
            analysis['minimum'] = number
        if number > analysis['maximum']:
            analysis['maximum'] = number

    # calculate the average
    analysis['average'] = analysis['sumTotal'] / len(list_parameter)

    analysis['length'] = len(list_parameter)

    # return the dictionary
    return analysis


returned_value = ultimate_analysis([37, 2, 1, -9])
print(returned_value)
