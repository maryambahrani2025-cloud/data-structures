def ins_befor(self,x,y):
 if self.head is None:
  print ('error0')
  return
c=self.head
while c:
 if c.Data==x:
  if c.Back is None:
   self.ins_First(y)
 Return
 a=dnode(y)
 a.next=c
 c.back.next=a
 a.back=c.back
 c.back=a
 Return
 c=c.next
 print('not found')