'''
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def inorder_traversal(self, node) -> list[int]:
        if node is None:
            return []
        return self.inorder_traversal(node.left) + [node.value] + self.inorder_traversal(node.right)


tree = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = Node(tree[0], Node(tree[1]), Node(tree[2]))
root.left.left = Node(tree[3])
root.left.right = Node(tree[4])
root.right.left = Node(tree[5])
root.right.right = Node(tree[6])

tree = Tree(root)
print(tree.inorder_traversal(tree.root))
