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
#balanced paraentesis
def is_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != matching[char]:
                return False

    return not stack

# Test cases
print(is_balanced("({[]})"))  # Output: True
print(is_balanced("({[)]"))  # Output: False


#stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
s = Stack()
s.push(5)
s.push(10)
s.push(15)
print("Top of the stack:", s.peek())  # Output: 15
print("Popped:", s.pop())  # Output: 15
print("Stack size:", s.size())  # Output: 2
#reverse polish notation
def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)

    return stack.pop()

print(evaluate_postfix("23*54*+"))  # Output: 26
#sort stack
def sort_stack(stack):
    temp_stack = []
    
    while stack:
        current = stack.pop()
        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())
        temp_stack.append(current)
    
    return temp_stack

stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sort_stack(stack)
print("Sorted stack:", sorted_stack)  # Output: [3, 23, 31, 34, 92, 98]
#undo redo
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def write(self, text):
        self.undo_stack.append(self.text)
        self.text += text
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def read(self):
        return self.text

# Usage
editor = TextEditor()
editor.write("Hello")
editor.write(", World!")
print("Text:", editor.read())  # Output: "Hello, World!"
editor.undo()
print("After Undo:", editor.read())  # Output: "Hello"
editor.redo()
print("After Redo:", editor.read())  # Output: "Hello, World!"
#stock span
def stock_span(prices):
    stack = []
    result = []

    for i, price in enumerate(prices):
        span = 1
        while stack and stack[-1][0] <= price:
            span += stack.pop()[1]
        stack.append((price, span))
        result.append(span)

    return result

prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))  # Output: [1, 1, 1, 2, 1, 4, 6]
#next greater element
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]
