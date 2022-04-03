def get_min_max(ints=[]):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    if isinstance(ints, list) == False or len(ints) == 0:
        return None
    min = -1
    max = -1
    for i in ints:
        if isinstance(i, int) == False:
            return None
        if min == -1:
            min = i
        elif i < min:
            min = i

        if max == -1:
            max = i
        elif i > max:
            max = i
    return (min, max)
       
       

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
l2 = [i for i in range(0, 10000000)]  # a list containing 0 - 9
random.shuffle(l)

#happy path
print('------------------happy path-------------------')
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") #pass
print ("Pass" if ((0, 9999999) == get_min_max(l2)) else "Fail") #pass

#edge cases
print('------------------edge cases-------------------')
print ("Pass" if (None == get_min_max(1)) else "Fail") #pass
print ("Pass" if (None == get_min_max(None)) else "Fail") #pass
print ("Pass" if (None == get_min_max((1,2,3,4))) else "Fail") #pass
print ("Pass" if (None == get_min_max([3,5,6,None,2])) else "Fail") #pass
print ("Pass" if (None == get_min_max([3,5,6,1.23])) else "Fail") #pass
print ("Pass" if (None == get_min_max()) else "Fail") #pass
print ("Pass" if (None == get_min_max([])) else "Fail") #pass
