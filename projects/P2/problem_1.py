def sqrt(number=None):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if isinstance(number, int) == False or number < 0:
        return None
    #https://en.wikipedia.org/wiki/Newton%27s_method#Square_root
    square_root = number
    estimate = (square_root + 1) / 2
    while estimate < square_root:
        square_root = estimate
        estimate = estimate - ((estimate * estimate - number) / (2 * estimate))
    return square_root // 1

# happy path
print('------------------happy path-------------------')
print ("Pass" if  (3 == sqrt(9)) else "Fail") #pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") #pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") #pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") #pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") #pass

# edge cases
print('------------------edge cases-------------------')
print ("Pass" if  (None == sqrt(None)) else "Fail") #pass
print ("Pass" if  (None == sqrt([])) else "Fail") #pass
print ("Pass" if  (None == sqrt(-1)) else "Fail") #pass
print ("Pass" if  (None == sqrt(55.12)) else "Fail") #pass
print ("Pass" if  (None == sqrt()) else "Fail") #pass
