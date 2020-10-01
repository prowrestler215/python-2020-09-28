def add(num1, num2):

    return num1 + num2
    # return


def run_test():
    return_value = add(1, 2)
    expected_return = 3

    # return return_value == expected_return
    if return_value == expected_return:
      return True
    else:
      return False

print(run_test())
