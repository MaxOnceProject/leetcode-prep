'''
116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000


Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, level: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.level = level
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self):
        self.tree = list()

    def __str__(self):
        return str(self.tree)

    def create_from_root(self, root: list[int]):
        max_count_for_current_level = 1
        level = 0
        position = 0
        for value in root:
            position += 1

            node = self._create_new_node(value, level)
            self._update_next(node=self._get_last_node_element_by_level(level), next_node=node)
            self._add_node_to_tree(node)

            if len(self._get_all_nodes_by_level(level)) == max_count_for_current_level:
                max_count_for_current_level *= 2
                level += 1

    def _create_new_node(self, value: int, level: int, left: 'Node' = None, right: 'Node' = None, next_node: 'Node' = None):
        return Node(val=value, level=level,left=left, right=right, next=next_node)

    def _add_node_to_tree(self, node):
        self.tree.append(node)

    def _update_next(self, node, next_node):
        if node:
            node.next = next_node

    def _get_all_nodes_by_level(self, level: int) -> list[Node]:
        return [node for node in self.tree if node.level == level]

    def _get_last_node_element_by_level(self, level: int):
        node_elements_by_level = self._get_all_nodes_by_level(level)
        if len(node_elements_by_level) == 0:
            return None
        return node_elements_by_level[-1]


root = [1, 2, 3, 4, 5, 6, 7]

tree = Tree()
tree.create_from_root(root)
print(tree.tree[1].next)
