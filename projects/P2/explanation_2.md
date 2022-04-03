For the rotated array search I decided to use recursive divide and conquer algorithm.  Using recursive we can iterate through each side of the pivot until we've found our element.

Space complexity: is O(n), our input_list contains every element in the list of numbers we are search for and does not change in size

Time complexity: is O(logn), by spliting our searching into two pieces we can divide the number of iterations quickly and since we know this list is sorted on either side we can effectively remove parts of the input list to find our goal