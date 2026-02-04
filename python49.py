def ins_after(self,x,y):
    if self.head is None:
        print('error0')
        return
    c=self.head
    while c:
     if c.Data==x:
       if c.next is None:
           self.ins_last(y)
           return
    a=dnode(y)
    a.next=c.next
    c.next=a
    a.next.back=a
    a.back=c
    return
c=c.next
print('not founde')