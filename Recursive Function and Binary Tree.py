#تابع بازگشتی
def rec(n):
    if "شرط بازگشت":
        return"مقداربارگشت "
    return "تعریف بازگشت"

#تابع بازگشتی بنویسید که فاکتوریل را حساب کند (nفاکتوریل)
def fact (n):
    if n==1:
        return1
    return fact (n-1)*n

#تابع بازگشتی بنویسید که حاصل ضرب دو عدد را محاسبه کند با فرض مثبت بودن اعداد
def zarb(a,b):
    if b==1:
        return a 
    return zarb(a,b-1)+a

#تابع بازگشتی بنویسید که حاصل تقسیم صحیح دو عدد مثبت را حساب کند 
def taghsim(a,b):
    if a<b:
        return0 
    return taghsim (a-b,b)+1

#کلاس درخت دودویی
class Tree_Node:
    def __init__(self , d):
        self.value=d
        self.Lchild=None
        self.Rchild=None

#تابع بازگشتی بنویسید که به صورت inorder درخت باینری را پیمایش کند و داده هایش را در خروجی چاپ کند 
def inorder (root):
    if root is None:
        return 
    inorder (root.Lchild)
    print (root.value)
    inorder(root.Rchild) 

#تابع بازگشتی بنویسید که به صورت postorder پیمایش شود و داده ها رو در خروجی چاپ کند 
def postorder (root):
    if root is None:
        return
    postorder(root.Lchild) 
    postorder(root.Rchild)
    print (root.value)

# تابعی بنویسید که ارتفاع درخت باینری را حساب کند 
def height (root):
    if root is None:
        return0
    return max (height(Lchild),height(R.child)+1) 

#تابع بازگشتی بنویسید کخ تعداد برگ های یک درخت دودویی را محاسبه کند
def count_leaves(root):
    if root is None:
        return 0
    if root.Rchild is None and root.Lchild is None:
        return 1
    return count_leaves (root.lchild)+count_leaves(root.Rchild)

#تابع بازگشتی بنویسید که تعداد گره های درجه یک درخت باینری را حساب کند 
def count_Nodes1D (root) :
    if root is None :
        return 0
    if root.Rchild is None and root.Lchild is not None:
        return 1+count_Nodes1D (root.Lchild)
    if root.Rchild is not None and root.Lchild is  None:
        return 1+count_Nodes1D (root.Rchild)
    if root.Rchild is None and root.Lchild is  None:
        return 0
    return count_Nodes1D (root.Rchild) + count_Nodes1D (root.lchild)+1

#تابع بنویسید که ماکسیمم داده یک درخت دودویی را بدست اورده و بازگرداند 
def max_T2 (root):
    if root is None :
        return 0
    return max (max_T2(root.Lchild), max_T2 (root.Rchild), root.value)

#تابع بازگشتی بنویسید که مینیمم داده یک درخت دودویی را بدست اورده و بازگرداند 
def minT2 (root):
    if root is None :
        return foolt ("inf")
    return min (minT2(root.Lchild), minT2 (root.Rchild), root.value)

# تابع بازگشتی بنویسید که محموع مقادیر گره های درخت را به ما بدهد
def sum_t2 (root):
    if root is None :
        return 0
    return sum_t2(sum_t2(root.Lchild), sum_t2(root.Rchild), root.value)