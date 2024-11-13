'''
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
import itertools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, root=None):
        self.val = val
        self.left = left
        self.right = right
        self.root = root

    def build(self):
        level = 1
        tree = list()
        numbers = list()
        for num in self.root:
            numbers += (num,)
            count = len(numbers)
            if count >= level:
                tree += [numbers]
                numbers = list()  # reset numbers
                level *= 2
        return tree

    def convert_to_root(self, tree):
        return list(itertools.chain(*tree))

    def invert(self):
        return [numbers[::-1] for numbers in self.build()]


root = [4, 2, 7, 1, 3, 6, 9]
Tree = TreeNode(root=root)
inverted_tree = Tree.invert()
print(Tree.convert_to_root(inverted_tree))
