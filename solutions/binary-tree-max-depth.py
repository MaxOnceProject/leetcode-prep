'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''


class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def calculate_max_depth(self, node: Node):
        if not node:
            return 0
        left_node = self.calculate_max_depth(node.left)
        right_node = self.calculate_max_depth(node.right)
        return 1 + max(left_node, right_node)

    def find_max_depth(self):
        return self.calculate_max_depth(self.root)


tree = [3,9,20,None,None,15,7]
root = Node(tree[0])
root.left = Node(tree[1])
root.right = Node(tree[2], left=Node(tree[5]), right=Node(tree[6]))
tree = Tree(root)
print(tree.find_max_depth())
