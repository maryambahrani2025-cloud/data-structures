def Del_first(self):
    if self.head is None:
        print('error0')
        return
    if self.head.next is None:
        c=self.head
        self.head=c.next 
        del c 
    if self.head:
        self.head.back=None
        del self.head
        self.head=None
        return