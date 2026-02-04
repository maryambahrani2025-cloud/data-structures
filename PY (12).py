def search(root,t):
    if root is None:
        return False
    if root.Data==t:
        return True
    return search(root.Lchild)or
search(root.Rchild)