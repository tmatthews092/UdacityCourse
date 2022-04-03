I decided to use sets for union and intersection since we do not want duplcates of any linked list. Additionally I chose to create dictionaries of the linked lists inorder to have quicker search times to determine if there was an intersection between two linked lists.

Union:
Time Complexity is O(nm), worst case scenario we loop through each element of each linked list m and n respectively
Space Complexity is O(nm), worst case scenario the size of the union set is the size of both linkedlists

Intersection:
Time Complexity is O(2n2m) or O(nm), worst case scenario we loop through each list twice first to create the dictionary then a second time to determine whether the element intersects
Space Complexity is O(n), worst case scenario all elements intersect and the size of the set is the same size as each list or just n 
