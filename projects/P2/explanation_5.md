For the data structure I am using a Dictionary. This contains each child, and its child along with the flag is_word.

Time complexity insert O(n), for each character in the word we'll need to add an entry into the dictionary
Time complexity find O(n) for each character in the word we'll need to continue our search until we find a word or not
Time complexity of suffix O(n)

Space complexity O(n*m) for each character in the word and m for each node