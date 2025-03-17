import logging
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def solution_tree(S, A):
    """
    Finds the longest alternating character path in a tree.
    """
    # Step 1: Build adjacency list for the tree
    tree = defaultdict(list)
    N = len(A)

    for child, parent in enumerate(A):
        if parent != -1:
            tree[parent].append(child)

    logging.debug(f"Tree structure: {dict(tree)}")  # Debug: Tree built

    # Step 2: DFS function to compute longest alternating path
    def dfs(node):
        logging.debug(f"DFS visiting node {node} ({S[node]})")  # Debug start

        max1, max2 = 0, 0  # Two longest alternating paths from this node

        for child in tree[node]:
            child_length = dfs(child)  # Recursively calculate longest path for child

            # Only consider if alternating character
            if S[child] != S[node]:
                if child_length > max1:
                    max2 = max1
                    max1 = child_length
                elif child_length > max2:
                    max2 = child_length

        # Update global max path
        nonlocal max_path
        max_path = max(max_path, max1 + max2 + 1)  # 1 for the current node

        logging.debug(f"Node {node}: max1={max1}, max2={max2}, max_path={max_path}")  # Debug computation

        return max1 + 1  # Return max path including this node

    # Step 3: Run DFS from root and compute max path
    max_path = 1
    dfs(0)

    logging.debug(f"Final max path: {max_path}")  # Debug result

    return max_path
