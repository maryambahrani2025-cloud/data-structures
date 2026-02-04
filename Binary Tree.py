#Binary Tree
class Tree_Node:
    def __init__(self,d):
        self.value=d
        self.RChild=None
        self.LChild=None

#insert
def insert(root,data):
        if root is None:
            return Tree_Node(data)
        if data < root.value :
            root.left = insert(root.left, data)
        else:
            root.right=insert(root.right,data)    
#inorder
def inorder(root):
        if root is None:
            return
        inorder(root.LChild)
        print(root.value)
        inorder(root.RChild)
#postorder
def postorder(root):
        if root is None:
            return
        postorder(root.Lchild)
        postorder(root.RChild)
        print(root.value)
#height of binary tree
def height(root):
    if root is None:    
        return 0
    return max(height(LChild),height(RChild))
#number of leaves in binary tree
def count_leaves(root):
    if root is None:
        return 0
    if root.Rchild is None and root.LChild is None :
            return 1
    return count_leaves(root.Lchild)+count_leaves(root.RChild)
#number of nodes D1 in binary tree
def count_nodesD1(root):
        if root is None:
            return 0
        if root.Rchild is None and root.LChild is not None :
            return 1+count_nodesD1(root.LChild)
        if root.Rchild is not None and root.LChild is None :
            return 1+count_nodesD1(root.RChild)
        if root.Rchild is None and root.LChild is None :
            return 0
        return   count_nodesD1(root.RChild) + count_nodesD1(root.LChild)
#number of nodes D2 in binary tree 
def count_nodesD2(root):
        if root is None:
            return 0
        if root.Rchild is None and root.LChild is not None :
            return count_nodesD2(root.LChild)
        if root.Rchild is not None and root.LChild is None :
            return count_nodesD2(root.RChild)
        if root.Rchild is None and root.LChild is None :
            return 0
        return 1+count_nodesD1(root.RChild) + count_nodesD1(root.LChild)
#value of maximum data in binary tree
def maxT2(root):
    if root is None:
        return float('-inf')
    return max(maxT2(root.RChild),maxT2(root.LChild),maxT2(root.value))
#value of minimum data in binary tree    
def minT2(root):
    if root is None:
        return float('inf')
    return min(minT2(root.RChild),minT2(root.LChild),minT2(root.value))
# summation of value of nodes
def sumT2(root):
    if root is None:
        return 0
    return sumT2(root.LChild)+sumT2(root.RChild)+sumT2(root.value)