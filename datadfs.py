# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS function
def dfs_recursive(node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(neighbor, visited)

# Usage
visited = set()
dfs_recursive('A', visited)
#DFS Using a Stack (Iterative)
# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS function
def dfs_iterative(start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Add neighbors to the stack

# Usage
dfs_iterative('A')

