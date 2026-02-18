def_Del_last(self):
  if self. head is None:
    print('error0')
    Return
   c=self.head
  while c.next
    c=c.next
  if c.back is None:
    self.Del_first()
    Return 
    c.back.next=None
    del c

