Given we have 1,0,2,0

The approach I took for this problem was to identify the value at the given index if its zero then move that to the zero pointer position so in this case in the second position we find the zero and switch with 1 then the zero pointer position becomes index 1. This will increment everytime we make a switch for zero. Then we do the same thing with two. If we encounter 2 in our example at the 2 index we switch with the two pointer which at that point would be the 3 index. At that point the array is sorted.

Time complexity is O(n), it takes a single traversal to sort all 0,1,2s
Space Complexity is O(1). There are no new data structures required for this in place sort