def min_T(root):
    if root is None:
        return false('Inf')
    return min(min_T(root.Lchild),min_T(root.Rchild),(root.Data))