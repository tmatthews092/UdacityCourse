For the data structure I am using a Dictionary. This contains each child, and its child along with the flag is_word.

Time complexity insert O(n), for each route in the path we'll need to add an entry into the dictionary
Time complexity find O(n) for each route in the path we'll need to continue our search until we find a handler or not

Space complexity O(n*m) for each route in the path and m for each node