class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    """
    Return the maximum depth of a binary tree.
    """
    if not root:
        return 0
    # Profundidad = 1 + máximo entre las profundidades de los subárboles
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    # Ejemplo: 
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(max_depth(root))  # 3