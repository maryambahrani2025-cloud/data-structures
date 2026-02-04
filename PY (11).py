def height(root):
  if root is None:
    return0
    return1+max(hight+(root.Rchild),height(root.Lchild))
        