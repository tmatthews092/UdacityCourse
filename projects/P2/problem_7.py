# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    def __init__(self):
        self.root = RouteTrieNode('root handler')
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    def insert(self, path, handler):
        current_node = self.root
        for i in range(len(path)):
            if i == len(path) - 1:
                current_node.insert(path[i], handler)
            else:
                current_node.insert(path[i])
            current_node = current_node.children.get(path[i])
    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    def find(self, path):
        current_node = self.root
        if len(path) == 1 and path == '/':
            return current_node
        for i in range(len(path)):
            current_node = current_node.children.get(path[i]) #needs to be moved above the return
            if current_node and i == len(path) - 1:
                return current_node

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    # Initialize the node with children as before, plus a handler
    def __init__(self, handler):
        self.handler = handler
        self.children = {}
    # Insert the node as before
    def insert(self, path, handler = None):
        if self.children.get(path) == None:
            self.children.update({path: RouteTrieNode(handler)})
    
    
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self):
        self.routes = RouteTrie()
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        if isinstance(path, str) and isinstance(handler, str):
            path = self.split_path(path)
            self.routes.insert(path, handler)
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, path):
        if isinstance(path, str) == False:
            return None
        path = self.split_path(path)
        route_node = self.routes.find(path)
        if route_node and route_node.handler:
            return route_node.handler
        return "not found handler"
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


    def split_path(self, path):
        if path.endswith('/'):
            path = path[:len(path)-1]
        return path.split('/')
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        
        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router() # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

#happy paths
# some lookups with the expected output
print('------------------happy path-------------------')
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

#edge cases
router.add_handler(None, "None handler")  # add a route
router.add_handler("None", None)  # add a route
router.add_handler(123, "number handler")  # add a route
router.add_handler("//", "double root handler")  # add a route
router.add_handler("/home//double_blackslash", "double backslash handler")  # add a route
router.add_handler("None", None)  # add a route
print('------------------edge cases-------------------')
print(router.lookup(None)) # should print 'None'
print(router.lookup("None")) # should print 'not found handler'
print(router.lookup(123)) # should print 'None'
print(router.lookup("123")) # should print 'not found handler'
print(router.lookup("//")) # should print 'double root handler'
print(router.lookup("/home//double_blackslash")) #should print 'double backslash handler'
