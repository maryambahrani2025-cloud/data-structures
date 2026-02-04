def Del_befor(self,x):
    if self.head is None:
     print('error0') 
     return 
    if self.head.Data==x:
        print('errorx')
        return 
    c=self.head 
    while c:
        if c.Data==x:
            a=c.dack
            c.back=a.back
            if a.back:
                a.back.next=c
                del a 
                return 
            c=c.next 
            print('x not found')   
