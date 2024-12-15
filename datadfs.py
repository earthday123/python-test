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

#DFS for Trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder DFS (Root, Left, Right)
def dfs_preorder(node):
    if node:
        print(node.value, end=" ")
        dfs_preorder(node.left)
        dfs_preorder(node.right)

# Inorder DFS (Left, Root, Right)
def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=" ")
        dfs_inorder(node.right)

# Postorder DFS (Left, Right, Root)
def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=" ")

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder:")
dfs_preorder(root)
print("\nInorder:")
dfs_inorder(root)
print("\nPostorder:")
dfs_postorder(root)
