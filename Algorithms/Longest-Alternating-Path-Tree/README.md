# Problem of the Longest Path that Can be Found in a Tree

You are given a tree consisting of $N$ nodes, numbered from $0$ to $N-1$. Each node contains one of the letters 'a' or 'b'.

* The tree is represented as an array $A$ of length $N$, where $A[K]$ (for $K$ from $0$ to $N-1$) denotes the parent of the K-th node.
* Node $0$ is the root and does not have a parent, so $A[0] = -1$.
* The letters in the nodes are represented as a string $S$, where $S[K]$ denotes the letter in the K-th node.

Your task is to find the number of vertices on the longest path in the tree, such that no pair of adjacent vertices contain the same letter.
