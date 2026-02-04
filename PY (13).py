def max_T(root):
 if root is None:
  return float('-Inf')
return max(max_T(root.Lchild),max_T(root.Rchild),(root.Data))