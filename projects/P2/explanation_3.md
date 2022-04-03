I decided to use a mergesort to rearrange the numbers into a sorted order since time complexity for that algorithm is O(nlogn). However I chose to rearrange from greatest to least (eg 3,2,1) then iterate again over the list and determine which element to choose based of the evens or odds place of the index.

Time complexity is O(nlogn) since I'm using the mergesort algorithm. I also reiterate over the array to determine the largest ints which is O(n), so O(2nlogn) or O(nlogn)

Space complexity is O(n)