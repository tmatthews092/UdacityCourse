import sys

class Node(object):
    def __init__(self, value=None, freqency=None):
        self.value = value
        self.frequency = freqency
        self.code = None
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value

    def set_frequency(self,frequency):
        self.frequency = frequency
        
    def get_frequency(self):
        return self.frequency

    def set_code(self,code):
        self.code = code
        
    def get_code(self):
        return self.code
    
    def get_left_node(self):
        return self.left
    
    def get_right_node(self):
        return self.right

def set_priority_queue(data):
    frequency_dict = {}
    for i in data:
        if frequency_dict.get(i) == None:
            frequency_dict[i] = Node(i, 1)
        else:
            frequency_dict[i].frequency += 1

    # Date: 1/13/2022, https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    return sorted(frequency_dict.values(), key=lambda node: node.frequency)

# Date: 1/13/2022, https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
def set_codes(node, codes={}, code=''):
        new_code = ''
        if node.get_code():
            new_code = code + node.get_code()
        if node.get_left_node():
            set_codes(node.get_left_node(), codes, new_code)
        if node.get_right_node():
            set_codes(node.get_right_node(), codes, new_code)
        if not node.get_left_node() and not node.get_right_node():
            codes.update({node.get_value(): new_code})
            
def huffman_encoding(data):
    if data is None:
        raise TypeError('Data cannot be None Type')
    #determine the frequency of each element in data
    #build the priority queue as when iterate
    priority_queue = set_priority_queue(data)
    while len(priority_queue) > 1: #if theres one node left its the root of the pq heap
        #iterate through the priority_queue fetching two mins
        min_node_1 = priority_queue[0]
        min_node_2 = priority_queue[1]

        #remove those two elements from the queue
        priority_queue = priority_queue[2:]

        #merge the two nodes
        merged_freq = min_node_1.frequency + min_node_2.frequency
        node_tree = Node(None, merged_freq)
        node_tree.left = min_node_1
        node_tree.right = min_node_2
        node_tree.left.code = '0'
        node_tree.right.code = '1'

        #add the nodetree back the priority queue
        priority_queue.append(node_tree)
        #resort to reset the priority queue
        priority_queue = sorted(priority_queue, key=lambda node: node.frequency)
        
    tree = priority_queue[0]
    codes = {}
    set_codes(tree, codes)
    encoded_data = ''
    for i in data:
        if codes.get(i):
            encoded_data += codes.get(i)
    return (encoded_data,tree)

def huffman_decoding(data,tree):
    decoded_data = ''
    current_node = tree
    for i in data:
        if i == '0':
            current_node = current_node.get_left_node()
        else:
            current_node = current_node.get_right_node()
        if not current_node.get_left_node() and not current_node.get_right_node():
            decoded_data += current_node.get_value()
            current_node = tree
    return decoded_data

if __name__ == "__main__":
    #Test One - Happy Path
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) #The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence)) #The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) #The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) #0110111011111100111000001010110000100011010011110111111010101011001010

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data)) #The content of the encoded data is: The bird is the word

    #Test Two - Catch None
    foundError = False
    try:
        encoded_data, tree = huffman_encoding(None)
    except:
        foundError = True
    print(foundError) # == True
    
    #Test Three - Lorem Ipsum
    
    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sed nisl facilisis, consequat erat a, tristique eros. Nunc volutpat ipsum id venenatis dapibus. Aliquam ut sagittis orci. Mauris dignissim laoreet ligula, a dictum nibh lacinia in. Curabitur accumsan semper posuere. Donec tempus neque vel urna mollis, nec dictum nisl porttitor. Etiam vitae feugiat lorem. Pellentesque rhoncus leo diam, eget venenatis nibh sollicitudin non. Cras scelerisque, eros a luctus facilisis, dui nulla sodales mauris, eu maximus ipsum felis in dui. Etiam tempus felis turpis, vitae fringilla justo tempor vitae. Donec odio massa, elementum at tellus ac, sodales fermentum sapien. Nullam lacus mi, lobortis eu vehicula sit amet, consequat eu libero.'\
    'Aliquam vel orci eget mauris feugiat iaculis. Vestibulum sollicitudin eleifend convallis. Nunc vel magna faucibus, iaculis tellus et, tincidunt dui. Integer efficitur eros vel lacus tristique dapibus id ut diam. Quisque consectetur nec metus in sollicitudin. Morbi vulputate justo libero, at tempus lectus luctus eu. Pellentesque porta blandit massa, sed cursus lectus pretium vitae. Ut viverra fringilla nisl eget blandit. Mauris ac tempus dolor, sed tristique sem. Suspendisse auctor lacus quis nisi porttitor, id sollicitudin nunc condimentum. Donec tempor dui molestie purus finibus, id tempus nisi fermentum.'\
    'Nullam tristique arcu sem, at mattis mi venenatis a. Nullam accumsan risus id lacinia varius. Phasellus a tincidunt felis. Pellentesque sollicitudin mi venenatis mauris gravida, quis bibendum nisl condimentum. Vestibulum id massa elementum, aliquam turpis vel, fringilla tortor. Nulla ligula lectus, semper non eros at, semper fringilla justo. Fusce et bibendum magna, at iaculis orci. Aenean interdum consectetur sapien, dignissim hendrerit dolor ultricies ut. Integer volutpat gravida erat vitae suscipit. Donec id accumsan sem. Integer congue dapibus eros sed ultricies. Etiam aliquam viverra dui, a imperdiet urna dictum fermentum.'\
    'Aliquam semper nisl dui, a iaculis libero elementum eget. Praesent condimentum ex lectus, eu consequat massa feugiat a. Duis porttitor molestie odio, ac vestibulum sapien imperdiet in. Vestibulum sit amet congue augue. Etiam scelerisque dignissim lacus eget fermentum. Quisque vitae mattis ex. In arcu tortor, consectetur sed bibendum eget, facilisis id sapien. In vel lectus tellus.'\
    'Aliquam erat volutpat. Vivamus sagittis fermentum pulvinar. Vivamus feugiat feugiat dignissim. Duis finibus lacinia ultricies. Quisque et lacus fringilla, rutrum nisl quis, facilisis felis. Praesent felis erat, sagittis eu magna sit amet, maximus efficitur ipsum. Nam pellentesque tellus ut sem congue, vitae consectetur enim ultricies. Suspendisse facilisis lacinia turpis, at gravida nisl mollis et. Aliquam erat volutpat.'\
    'Nullam non finibus urna, sit amet laoreet odio. Proin eu dolor sit amet ex feugiat fringilla ut dictum magna. Phasellus vitae libero a elit vulputate fermentum sit amet at magna. Donec quis ipsum lectus. Pellentesque tempor est et sagittis venenatis. Aliquam vel elementum tortor. Maecenas lacinia ex sed leo efficitur viverra. Nam feugiat consequat eros quis facilisis. Nulla iaculis felis mauris, sed euismod nibh luctus in. Donec et consequat lectus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec vitae ante tristique magna tempus mollis. Quisque scelerisque ornare nibh, quis tincidunt nulla semper at. Proin a blandit erat, eu pulvinar ex. Vestibulum pulvinar, tellus id accumsan lobortis, dui augue eleifend diam, faucibus aliquet arcu magna vitae lorem. Cras et aliquet lacus, at hendrerit nunc.'\
    'Phasellus consectetur ante sit amet mattis rutrum. Nulla non lectus ac dolor scelerisque tempor. Nulla et laoreet magna, vitae imperdiet velit. Ut ullamcorper leo quis lacus luctus, efficitur accumsan libero suscipit. Aliquam congue consectetur feugiat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'\
    'Proin eget dictum nulla, vel congue quam. Fusce cursus consectetur neque non efficitur. Quisque suscipit arcu est, id congue libero viverra id. Donec pellentesque viverra enim, eget viverra lacus accumsan in. Quisque lobortis mollis risus, ac egestas metus mollis eget. Quisque rutrum, massa ac sodales convallis, odio turpis pulvinar sapien, vitae finibus libero neque a ex. Suspendisse eu elit vel lorem varius accumsan nec id nisl. Praesent elementum mauris nibh. Ut eu rutrum eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam efficitur, tortor nec rhoncus vehicula, sem dolor congue justo, a iaculis ante lectus eget lectus. Quisque laoreet commodo magna sed aliquet.'\
    'Nulla facilisi. Aenean et neque vitae nisi mollis elementum quis nec purus. Mauris eget viverra ex, ut cursus augue. Sed hendrerit aliquam gravida. Pellentesque ac bibendum diam. Phasellus nec dolor et ipsum feugiat ultrices sed vitae dolor. Maecenas tempus eros nec ullamcorper efficitur. Nunc justo mauris, convallis eget purus eu, vulputate porta risus. Pellentesque aliquet sagittis nunc, id auctor turpis fringilla in. Aliquam venenatis nisi diam, sit amet finibus ex viverra ac. Donec aliquam mollis commodo. Suspendisse nec lacus justo. Proin a risus nisl.'\
    'Morbi scelerisque mauris tellus, et facilisis mauris auctor sed. Vestibulum et leo aliquet, ullamcorper arcu a, elementum quam. Proin non neque lacinia neque mollis egestas non vel erat. Nulla a justo efficitur libero luctus ultricies. Proin vitae ligula mollis, tempor mi et, tincidunt nisi. Curabitur vulputate placerat leo, ut venenatis magna pulvinar a. Nunc maximus urna sem, ac pretium leo gravida et. Donec risus magna, euismod id euismod pellentesque, pellentesque ac nisi.'
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(lorem_ipsum))) #The size of the data is: 5946
    # print ("The content of the data is: {}\n".format(lorem_ipsum))

    encoded_data, tree = huffman_encoding(lorem_ipsum)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) #The size of the encoded data is: 3372
    # print ("The content of the encoded data is: {}\n".format(encoded_data)) #

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #The size of the decoded data is: 5946
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
    print ("The decoded size should equal the expected: {}\n".format(sys.getsizeof(decoded_data) == sys.getsizeof(lorem_ipsum))) #True
    print ("Provided data and decoded data should equal each other: {}\n".format(decoded_data == lorem_ipsum)) #True
