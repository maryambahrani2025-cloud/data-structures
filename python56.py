def Del_x(self,x):
    if self.head is None:
        print('error')
        return 
    if self.head.Data==x
    self.Del.First()
    return 
c=self.head 
while c:
    if c.next is None:
        self.Del_last()
        Return 
    c.back.next=c.next 
    c.next.back=c.back
    del c
    Return
c=c.next 
print('not found')