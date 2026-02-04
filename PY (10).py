def count(root):
    if root is None:
      return0
      return1+count(root.Lchild)
      +count(root.Rchild)
        