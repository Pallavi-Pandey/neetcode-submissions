"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            print("Input node is None, returning None")
            return None

        old_to_new = {}

        def dfs(curr):
            print(f"\nEntering dfs({curr.val})")

            # already cloned
            if curr in old_to_new:
                print(f"Node {curr.val} already cloned → returning copy")
                return old_to_new[curr]

            # clone current node
            print(f"Cloning node {curr.val}")
            copy = Node(curr.val)
            old_to_new[curr] = copy
            print(f"Mapping: original {curr.val} → copy {copy.val}")

            # clone neighbors
            for n in curr.neighbors:
                print(f"Node {curr.val} → visiting neighbor {n.val}")
                copy_neighbor = dfs(n)
                copy.neighbors.append(copy_neighbor)
                print(
                    f"Added edge: copy({copy.val}) → copy({copy_neighbor.val})"
                )

            print(f"Exiting dfs({curr.val})")
            return copy

        print("Starting DFS cloning...\n")
        result = dfs(node)
        print("\nCloning completed.")
        return result
