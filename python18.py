defInsert.last(self,x)
if self.head is None:
    self.head=node(x)
else:
    a=node(x)
    c=self.head
while c.next:
 c.next=a   
        