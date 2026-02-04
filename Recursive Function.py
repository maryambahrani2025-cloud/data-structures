#Recursive Function
# محاسبه فاکتوریل
def fact(n):
    if n==1:
        return 1
    return fact (n-1)*n
#حاصل ضرب دو عدد بزرگتر از صفر 
def zarb(a,b):
    if b==1:
        return a
    return zarb(a,b-1)+a
#حاصل تقسیم دو عدد بزرگتر از صفر
def tagh(a,b):
    if a<b:
        return 0
    return tagh(a-b,b)+1
