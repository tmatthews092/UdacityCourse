I chose to use a priority queue to contain all the node with frequencies. This way I'd have the minimum frequency nodes first which could be combined to form a tree. Then I could readd them to the tree and sort to reevaluate the min frequency nodes. 

The time complexity for the huffman encoding is O(n^2 log n). I'm using a sort within a loop, which is causing there to be a loop within a loop. Causing the algorithm to iterate over itself again to sort the elements within the list
https://stackoverflow.com/questions/58259035/time-complexity-of-sorting-inside-while-loop

Space Complexity for encoding is O(nm), since I'm using the priority queue to sort elements (n), which is relatively as big as the data provided and (m) for the amount of codes in the dictionary

The time complexity for decoding is O(n) since we iterate through the encoded data, which is dependent on the size of the data itself.
