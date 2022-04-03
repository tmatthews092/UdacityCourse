def sort_012(input_list=[]):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if isinstance(input_list, list) == False or len(input_list) == 0:
        return None
    if len(input_list) == 1 and input_list[0] == None:
        return None
    zero_pointer = 0
    two_pointer = len(input_list) - 1
    i = 0
    while i <= two_pointer and zero_pointer < two_pointer:
        if is_valid_input(input_list[i]) == False:
            return None
        if input_list[i] == 0:
            i_val = input_list[i]
            zero_pointer_val = input_list[zero_pointer]
            input_list[i] = zero_pointer_val
            input_list[zero_pointer] = i_val
            zero_pointer += 1
            i += 1
        elif input_list[i] == 2:
            i_val = input_list[i]
            two_pointer_val = input_list[two_pointer]
            input_list[i] = two_pointer_val
            input_list[two_pointer] = i_val
            two_pointer -= 1
        else:
            i += 1
    return input_list
        
def is_valid_input(value):
    is_valid = True
    if isinstance(value, int) == False:
        is_valid = False
    elif value > 2 or value < 0:
        is_valid = False
    return is_valid             
        

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
        
#happy path
print('------------------happy path-------------------')
test_function([2,0,1,2,0,1])
test_function([1,2,0,1,2,0])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#edge cases
print('------------------edge cases-------------------')
print ("Pass" if  (None == sort_012(None)) else "Fail") #pass
print ("Pass" if  (None == sort_012([None])) else "Fail") #pass
print ("Pass" if  (None == sort_012([None,1])) else "Fail") #pass
print ("Pass" if  (None == sort_012([None,2,0,1])) else "Fail") #pass
print ("Pass" if  (None == sort_012([1.23,2,1,0])) else "Fail") #pass
print ("Pass" if  (None == sort_012([3,1,0,1,2])) else "Fail") #pass
print ("Pass" if  (None == sort_012([])) else "Fail") #pass
print ("Pass" if  (None == sort_012()) else "Fail") #pass
