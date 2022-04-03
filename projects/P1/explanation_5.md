I decided to use a list for the Blockchain. The list appends each Block and uses its length to determine index for the Block and index-1 to fetch the previous hash. Using index-1 for the previous hash allows us to have a linkedlist. The list is easily iterated over and allows us to easily add and verify the block chain.

Time Complexity calc_hash, encoding for utf-8 is O(n).
Space Complexity calc_hash, we're using a fixed amount of space each time O(1)

Time Complexity get_block_chain, we're looping through the list twice once to determine its validity O(n) and again to add each element to print O(n) so O(2n) = O(n)

Space Complexity get_block_chain is O(n) since we're creating a separate list to contain all the values we want to print