#Sorting
#None-In-Place-Sort
A=[5,7,11,0,-3]
def sort1(A):
    B=[]*len(A)
    for j in range(len(A)):
        min=A[0]
        k=0 
        for i in range(1,len(A)):
            if A[i]<min:
                min=A[i]
                k=i
        B[j]=min
        A[k]=float('inf')
    return B
#In-Place-Sort
def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                