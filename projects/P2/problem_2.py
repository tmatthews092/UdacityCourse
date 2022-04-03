def rotated_array_search(input_list=[], number=None):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    if isinstance(number, int) == False or isinstance(input_list, list) == False:
        return -1
    list_length = len(input_list)
    if list_length == 0 or number < 0:
        return -1
    return recurse_array(input_list, number, 0, list_length - 1)

def recurse_array(input_list, number, start, end):
    pivot = (start + end) // 2
    if isinstance(input_list[pivot], int) and input_list[pivot] == number:
        return pivot
    elif (
            isinstance(input_list[start], int) and 
            input_list[start] <= number and 
            number in input_list[:pivot]
        ):
        return recurse_array(input_list, number, start, pivot - 1)
    elif (
            isinstance(input_list[end], int) and 
            input_list[end] >= number and 
            number in input_list[(pivot+1):]
        ):
        return recurse_array(input_list, number, pivot + 1, end)
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

#happy path
print('------------------happy path-------------------')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #pass

# #edge cases
print('------------------edge cases-------------------')
test_function([[], 10]) #pass
print ("Pass" if -1 == rotated_array_search(None, 10) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search([-1], 10) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search([1.23], 10) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search([None], 10) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], -1) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], None) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1.23) else "Fail") #pass
print ("Pass" if -1 == rotated_array_search() else "Fail") #pass
