from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Stores key-value pairs
        self.order = deque()  # Maintains the order of keys for LRU eviction

    def get(self, key):
        """
        Retrieve a value from the cache.
        """
        if key in self.cache:
            # Move the key to the front (most recently used)
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        return -1  # Key not found

    def put(self, key, value):
        """
        Add or update a key-value pair in the cache.
        """
        if key in self.cache:
            # Update value and move key to the front
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item
                lru_key = self.order.pop()  # Remove the least recently used key
                del self.cache[lru_key]
            # Add the new key-value pair
            self.cache[key] = value
            self.order.appendleft(key)

    def display(self):
        """
        Display the current state of the cache.
        """
        print("Cache content:", self.cache)
        print("Order (Most Recently Used -> LRU):", list(self.order))


# Example Usage
lru = LRUCache(3)

# Adding items
lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")
lru.display()

# Accessing an item (makes it most recently used)
print(lru.get(2))  # Output: "B"
lru.display()

# Adding a new item (evicts the least recently used item, which is key 1)
lru.put(4, "D")
lru.display()

# Accessing a non-existent item
print(lru.get(1))  # Output: -1 (key 1 was evicted)

# Updating an item
lru.put(3, "C updated")
lru.display()
# Using a Python list as a stack
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after pushing:", stack)  # Output: [1, 2, 3]

# Pop elements from the stack
print("Popped:", stack.pop())  # Output: 3
print("Popped:", stack.pop())  # Output: 2

print("Stack after popping:", stack)  # Output: [1]


from collections import deque

stack = deque()

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushing:", stack)  # Output: deque([10, 20, 30])

# Pop elements from the stack
print("Popped:", stack.pop())  # Output: 30
print("Popped:", stack.pop())  # Output: 20

print("Stack after popping:", stack)  # Output: deque([10])

#reversing string
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

print(reverse_string("hello"))  # Output: "olleh"
