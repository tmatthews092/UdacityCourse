class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_dict(self):
        out = {}
        node = self.head
        while node:
            out.update({node.value: node.value})
            node = node.next
        return out

def union(llist_1, llist_2):
    union_set = set()
    
    llist_1_node = llist_1.head
    llist_2_node = llist_2.head
    try:
        while llist_1_node:
            if llist_1_node.value:
                union_set.add(llist_1_node.value)
            llist_1_node = llist_1_node.next
        while llist_2_node:
            if llist_2_node.value:
                union_set.add(llist_2_node.value)
            llist_2_node = llist_2_node.next
    except Exception as e:
        print('Error during linked list union: ' + str(e))
        return None
    return union_set

def intersection(llist_1, llist_2):
    intersection_set = set()
    
    try:
        dict_1 = llist_1.to_dict()
        dict_2 = llist_2.to_dict()

        for i in dict_1.keys():
            if dict_2.get(i):
                intersection_set.add(i)
        for i in dict_2.keys():
            if dict_1.get(i):
                intersection_set.add(i)
    except Exception as e:
        print('Error during linked list intersection: ' + str(e))
        return None
    return intersection_set
    


print('\n Test One - Happy Path')
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# {32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21}
# {4, 21, 6}

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# {65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23}
# set()

# Test Two
print('\nTest Two - Mixed Valid/Invalid Values')

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [None,None,65,'12312',(12,12),3,'asdasb']
element_2 = [1,7,None,9,(12,12),21,'asdasb']

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
# {65, 1, 3, 7, 9, (12, 12), 21, 'asdasb', '12312'}
# {'asdasb', (12, 12)}

# Test Three
print('\nTest Three - Invalid Values')

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1,2,3,4,[1,2,3,4],1]
element_2 = [1,23,3,4,56,6]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)
    
print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))
# Error during linked list union: unhashable type: 'list'
# None
# Error during linked list intersection: unhashable type: 'list'
# None

# Test Four
print('\nTest Four - Empty Lists')

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

print (union(linked_list_9,linked_list_10))
print (intersection(linked_list_9,linked_list_10))
# set()
# set()