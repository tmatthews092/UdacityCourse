from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}
    
    def insert(self, char, is_word=False):
        ## Add a child node in this Trie
        if self.children.get(char) == None:
            self.children.update({char: TrieNode(is_word)})
    
    def suffixes(self):
        return suffix_recurse(self,'',[])

def suffix_recurse(node, suffix='', suffix_array=[]):
    if node.is_word:
        # if the child is last and is_word then add suffix to array
        suffix_array.append(suffix)
    for key in node.children.keys():
        # trying to recurse through the children and if any have children dive deeper
        key_node = node.children.get(key)
        suffix_recurse(key_node, suffix+key, suffix_array)
    return suffix_array
    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word=None):
        ## Add a word to the Trie
        if isinstance(word, str) == False:
            return
        current_node = self.root
        for i in range(len(word)):
            if i == len(word) - 1:
                current_node.insert(word[i], True)
            else:
                current_node.insert(word[i])
            current_node = current_node.children.get(word[i])
    
    def find(self, prefix=None):
        if isinstance(prefix, str) == False:
            return None
        current_node = self.root
        for i in range(len(prefix)):
            current_node = current_node.children.get(prefix[i])
            if current_node == None:
                return None
            elif current_node and i == len(prefix) - 1:
                return current_node

#happy path
print('------------------happy path-------------------')
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        print('prefix is ' + prefix)
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


#edge cases
print('------------------edge cases-------------------')
trie = Trie()
trie.insert(None)
trie.insert(1234)
trie.insert('1234')
trie.insert('\'hello!\'')
trie.insert()

print ("Pass" if  (None == trie.find('a')) else "Fail") #pass
print ("Pass" if  (None == trie.find()) else "Fail") #pass
print ("Pass" if  (['234'] == trie.find('1').suffixes()) else "Fail") #pass
print ("Pass" if  (None == trie.find('h')) else "Fail") #pass
print ("Pass" if  (['hello!\''] == trie.find('\'').suffixes()) else "Fail") #pass

trie.insert('abcdefghijklmnopqrstuvwxyz')
trie.insert('antidisestablishmentarianism')
print ("Pass" if  (['bcdefghijklmnopqrstuvwxyz', 'ntidisestablishmentarianism'] == trie.find('a').suffixes()) else "Fail") #pass
