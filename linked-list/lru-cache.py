class Node:
    def __init__(self,key=0,val=0):
        self.key,self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self,capacity):
        self.cap = capacity
        self.cache = {}
        self.left,self.right = Node(),Node()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self,node):
        prev,next = node.prev,node.next
        prev.next = next
        next.prev = prev

    def insert(self,node):
        prev,next = self.right.prev,self.right
        prev.next = next.prev = node
        node.prev,node.next = prev,next
    
    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            lru.next.prev,self.left.next = self.left,lru.next
            del self.cache[lru.key]