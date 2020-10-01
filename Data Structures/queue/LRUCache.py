class LRUCache:
    def __init__(self, n):
        # store keys of cache
        self.deque= []
        # store reference of key in cache
        self.hash = dict() 
        self.csize = n # max capacity of cache

    def refer(self, x):
        # if current page is not present in the cache
        if not self.hash.get(x):
            # if cache is full
            if len(self.deque) == self.csize:
                # delete the least recently used element from cache
                last = self.deque.pop()
                # delete that element from the hash map
                self.hash.pop(last)
        # if the current page is present in the cache
        else:
            # delete found element from cache
            self.deque.remove(self.hash[x])
        # add the current page at the front
        self.deque.insert(0, x)
        #update the hashmap
        self.hash[x] = self.deque[0]

    def display(self):
        for i in range(0, len(self.deque)):
            print(self.deque[i], end=' ')
        print()

lru = LRUCache(4)
lru.refer(1)
lru.display()
lru.refer(2)
lru.display()
lru.refer(3)
lru.display()
lru.refer(1)
lru.display()
lru.refer(4)
lru.display()
lru.refer(5)
lru.display()
