# ---------------------------------------------------------
# Title: Find All Duplicates in an Array
#
# Description:
#   Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
#   1
#
# Example 2:
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
#   7
#
# Creating Date: Jun 20
# Latest Rectifying: Jun 20
# ---------------------------------------------------------


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solution1(root):
    """
    Solution by myself
    ---
    :type root: TreeNode
    :rtype: int
    """

    queue = [root]
    bfs_nodes = []  # Save nodes with the order indicated by BFS

    while queue:
        cur_node = queue.pop(0)
        bfs_nodes.append(cur_node)
        if cur_node.right is not None:
            queue.append(cur_node.right)
        if cur_node.left is not None:
            queue.append(cur_node.left)

    return bfs_nodes[-1].val


def main():

    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    left_bottom1 = solution1(root1)
    print(left_bottom1)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.right.left.left = TreeNode(7)
    left_bottom2 = solution1(root2)
    print(left_bottom2)


if __name__ == '__main__':

    main()
