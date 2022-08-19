"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出二叉树。
"""

preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]
# postorder 后序


class BinaryTreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def construct(preorder, inorder):
    if preorder is None or inorder is None or len(preorder) == 0 or len(preorder) != len(inorder):
        return

    return construct_core(preorder, inorder)


def construct_core(preorder, inorder):

    root = BinaryTreeNode()
    if len(preorder) == 0:
        return root

    root_value = preorder[0]
    root.value = root_value

    root_inorder = None
    for index, item in enumerate(inorder):
        if item == root_value:
            root_inorder = index

    left_inorder = inorder[:root_inorder]
    right_inorder = inorder[root_inorder+1:]

    if len(left_inorder):
        root.left = construct_core(preorder[1:len(left_inorder)+1], left_inorder)

    if len(right_inorder):
        root.right = construct_core(preorder[len(right_inorder):], right_inorder)

    return root


binary_tree = construct(preorder, inorder)

