from collections import defaultdict

# Example 1: Grouping names by their first letter
names = ["Alice", "Bob", "Charlie", "Anna", "Brian"]
grouped_names = defaultdict(list)

for name in names:
    grouped_names[name[0]].append(name)

print(dict(grouped_names))
# Output: {'A': ['Alice', 'Anna'], 'B': ['Bob', 'Brian'], 'C': ['Charlie']}


# Example 2: Counting occurrences of items
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

print(dict(word_count))
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


# Example 3: Nested defaultdict for a matrix
matrix = defaultdict(lambda: defaultdict(int))
matrix[0][1] = 5
matrix[1][2] = 3

print(matrix[0][1])  # Output: 5
print(matrix[2][3])  # Output: 0 (default value)


# Example 4: Defaultdict with a set
tags = [("Alice", "Python"), ("Bob", "Java"), ("Alice", "Java")]
user_tags = defaultdict(set)

for user, tag in tags:
    user_tags[user].add(tag)

print(dict(user_tags))
# Output: {'Alice': {'Python', 'Java'}, 'Bob': {'Java'}}


# Example 5: Avoiding KeyError for missing keys
dd = defaultdict(str)
print(dd["missing_key"])  # Output: '' (default value is an empty string)


# Example 6: Caching computed values
import math
sqrt_cache = defaultdict(float)

for i in range(5):
    sqrt_cache[i] = math.sqrt(i)

print(dict(sqrt_cache))
# Output: {0: 0.0, 1: 1.0, 2: 1.4142135623730951, 3: 1.7320508075688772, 4: 2.0}


# Example 7: Initializing with default values
scores = defaultdict(lambda: 10)  # Default score is 10
scores["Alice"] += 5
scores["Bob"] += 2

print(dict(scores))
# Output: {'Alice': 15, 'Bob': 12}


# Example 8: Accumulating values
sales = [("Alice", 100), ("Bob", 200), ("Alice", 300)]
total_sales = defaultdict(int)

for name, amount in sales:
    total_sales[name] += amount

print(dict(total_sales))
# Output: {'Alice': 400, 'Bob': 200}


# Example 9: Defaultdict with custom objects
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __repr__(self):
        return str(self.count)

custom_dd = defaultdict(Counter)

custom_dd["item1"].increment()
custom_dd["item2"].increment()
custom_dd["item1"].increment()

print(dict(custom_dd))
# Output: {'item1': 2, 'item2': 1}


# Example 10: Defaultdict for simple caching
cache = defaultdict(lambda: "Not Found")
cache["key1"] = "value1"
print(cache["key1"])  # Output: value1
print(cache["key2"])  # Output: Not Found (default value)
