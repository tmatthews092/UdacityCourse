I used a list here since it would be the easiest data structure to work with since we need to append each file to the list and report that it exists. I decided to use another function which would contain the list of appended matched files. Then pass the path and suffix. The recursion is then used to navigate into each directory to then append the matching files.

We call the recursive function within the loop where path is the parameter which can be any n amount of elements we need to iterate over so we end up with O(n!).

Space complexity is O(mn) since max depth O(m) and O(n) is the amount of files that could be stored given the algorithm