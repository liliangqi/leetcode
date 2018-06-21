# ---------------------------------------------------------
# Title: Find Largest Value in Each Tree Row
#
# Description:
#   You need to find the largest value in each row of a binary tree.
#
# Example:
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
# Output:
#       [1, 3, 9]
#
# Creating Date: Jun 21
# Latest Rectifying: Jun 21
# ---------------------------------------------------------


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def solution1(root):
    """
    Inefficient solution by myself
    ---
    Runtime: 252ms
    ---
    :type root: TreeNode
    :rtype: list[int]
    """

    if root is None:
        return []

    queue = [(root, 0)]
    bfs_nodes = []
    output = []
    cur_depth = 0

    while queue:
        bfs_nodes.append(queue.pop(0))
        cur_node, cur_depth = bfs_nodes[-1]
        if cur_node.left is not None:
            queue.append((cur_node.left, cur_depth + 1))
        if cur_node.right is not None:
            queue.append((cur_node.right, cur_depth + 1))

    for i in range(cur_depth + 1):
        exec('row{} = []'.format(i))
    for node in bfs_nodes:
        exec('row{}.append(node[0].val)'.format(node[-1]))
    for i in range(cur_depth + 1):
        exec('output.append(max(row{}))'.format(i))

    return output


def solution2(root):
    """
    Inefficient solution by myself
    ---
    Runtime: 72ms
    ---
    :type root: TreeNode
    :rtype: list[int]
    """

    if root is None:
        return []

    queue = [(root, 0)]
    bfs_nodes = []

    while queue:
        bfs_nodes.append(queue.pop(0))
        cur_node, cur_depth = bfs_nodes[-1]
        if cur_node.left is not None:
            queue.append((cur_node.left, cur_depth + 1))
        if cur_node.right is not None:
            queue.append((cur_node.right, cur_depth + 1))

    split = [[bfs_nodes[0][0].val]]
    for x, y in zip(bfs_nodes[:-1], bfs_nodes[1:]):
        if x[1] == y[1]:
            split[-1].append(y[0].val)
        else:
            split.append([y[0].val])

    return [max(vals) for vals in split]


def solution3(root):
    """
    Idea from other guy
    ---
    Runtime: 60ms
    ---
    :type root: TreeNode
    :rtype: list[int]
    """

    if root is None:
        return []

    queue = [root]
    output = []
    while queue:
        output.append(max([i.val for i in queue]))
        q_temp = []
        for node in queue:
            if node.left is not None:
                q_temp.append(node.left)
            if node.right is not None:
                q_temp.append(node.right)
        queue = q_temp

    return output


def main():

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    output = solution2(root)
    print(output)


if __name__ == '__main__':

    main()
