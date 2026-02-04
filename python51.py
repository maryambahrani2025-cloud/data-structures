def ins_befor(self,x,y):
    if self.head is None:
        print('errore')
        return
    c=self.head 
    while c:
        if c.Data==x:
            if c.back is None:
                self.ins_first(y)
                return 
            a=dnode(y)
            a.next=c
            c.back.next=a
            a.back=c.next
            c.back=a 
            return 
        c=c.next 
        print('not found')