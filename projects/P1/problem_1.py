class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def set_recent_node(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        
    def evict_node(self,node):
        node_prev = node.prev
        node_next = node.next
        node_next.prev = node_prev
        node_prev.next = node_next


class LRU_Cache(object):
    
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.num_entries = 0
        self.hash_map = {}
        self.linked_list = DoublyLinkedList()
        self.linked_list.head = Node(-1, -1) #dummy head
        self.linked_list.tail = Node(-1, -1) #dummy tail
        self.linked_list.head.next = self.linked_list.tail
        self.linked_list.tail.prev = self.linked_list.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.hash_map.get(key) == None:
            return -1
        self.linked_list.evict_node(self.hash_map.get(key))
        self.linked_list.set_recent_node(self.hash_map.get(key))
        return self.hash_map.get(key).value

    def set(self, key, value):
        if self.num_entries == self.capacity:
            del self.hash_map[self.linked_list.tail.prev.key]
            self.linked_list.tail = self.linked_list.tail.prev
            self.hash_map.update({key:Node(key,value)})
            self.linked_list.set_recent_node(self.hash_map.get(key))
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        elif self.hash_map.get(key) != None:
            self.hash_map.get(key).value = value
            self.linked_list.evict_node(self.hash_map.get(key))
            self.linked_list.set_recent_node(self.hash_map.get(key))
        else:
            self.hash_map.update({key:Node(key,value)})
            self.linked_list.set_recent_node(self.hash_map.get(key))
            self.num_entries += 1
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))       # returns 1

print(our_cache.get(2))       # returns 2

our_cache.set(5, 5) 

# Test One Check Heads/Tails
print(our_cache.num_entries) # == 5
print(our_cache.linked_list.head.next.key) # == 5
print(our_cache.linked_list.head.next.value) # == 5
print(our_cache.linked_list.tail.prev.key) # == 3
print(our_cache.linked_list.tail.prev.value) # == 3


our_cache.set(6, 6)


# Test Two Check Not present cache and recently popped
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


#Test Three Check if None works within the cache
our_cache.set(None, None)
print(our_cache.num_entries) # == 5
print(our_cache.linked_list.head.next.key) # == None
print(our_cache.linked_list.head.next.value) # == None
print(our_cache.linked_list.tail.prev.key) # == 1
print(our_cache.linked_list.tail.prev.value) # == 1
