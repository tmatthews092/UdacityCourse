from re import I


def rearrange_digits(input_list=[]):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if isinstance(input_list, list) == False or len(input_list) < 2:
        return None
    input_list = mergesort(input_list)
    two_maximum_sums = ['','']
    for i in range(len(input_list)):
        if is_valid_input(input_list[i]) == False:
            return None
        if i % 2 == 0:
            two_maximum_sums[0] += str(input_list[i])
        else:
            two_maximum_sums[1] += str(input_list[i])
    two_maximum_sums[0] = int(two_maximum_sums[0])
    two_maximum_sums[1] = int(two_maximum_sums[1])
    return two_maximum_sums

def is_valid_input(value):
    is_valid = True
    if isinstance(value, int) == False:
        is_valid = False
    elif value > 9 or value < 0:
        is_valid = False
    return is_valid

def mergesort(items):
    
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return reverse_merge(left, right)
    
def reverse_merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#happy path
print('------------------happy path-------------------')
test_function([[1, 2, 3, 4, 5], [531, 42]]) #pass
test_function([[1, 2], [2, 1]]) #pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) #pass
test_function([[0,0,0,0,1,0,0,0,0],[10000, 0000]]) #pass

#edge cases
print('------------------edge cases-------------------')
print ("Pass" if  (None == rearrange_digits(None)) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits([None])) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits([])) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits()) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits([2])) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits([1,2,3,4,-1])) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits([1.23,1,2,3])) else "Fail") #pass
print ("Pass" if  (None == rearrange_digits([123,1,2,3])) else "Fail") #pass
