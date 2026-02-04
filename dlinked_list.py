class dnode:
    def __init__(self,x):
        self.Data=x
        self.back=None
        self.next=None
class dlinked_list:
    def __init__(self):
        self.head=None
    def ins_first(self,x) :
        if self.head is None:
            self.head=dnode(x)
            return
        a=dnode(x)
        a.next=self.head
        self.head.back=a
        self.head=a
    def ins_last(self,x):
        if self.head is None:
            self.head=dnode(x)
            return
        c=self.head
        while c.next:
            c=c.next
        a=dnode(x) 
        c.next=a
        a.back=c
    def ins_after(self,x,y):
        if self.head is None:
            print("error 0")
            return
        c=self.head
        while c:
            if c.Data == x :
                if c.next is None :
                    self.ins_last(y)
                    return
                a=dnode(y)
                a.next=c.next
                c.next=a
                a.next.back=a
                a.back=c
                return
            c=c.next
        print("not found")
    def ins_before(self,x,y):
        if self.head is None:
            print("error 0")
            return
        c=self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.ins_first(y)
                    return
                a=dnode(y)
                a.next=c
                a.back=c.back
                c.back.next=a
                c.back=a
                return
            c=c.next
        print("not found")   
    def Del_first(self):
            if self.head is None:
                print("error 0")
            else:
                c=self.head
                self.head=c.next
                del c
                if self.head :
                    self.head.back=None
                    return
    def Del_last(self):
        if self.head is None:
            print("error 0")
            return
        if self.head.next is None :
            self.Del_first()
            return
        c=self.head
        while c.next.next:
            c=c.next
        del c.next
        c.next=None
    def Del_after(self,x):
        if self.head is None:
            print("error 0")
            return
        c=self.head
        while c:
            if c.Data ==x :
                if c.next:
                    a=c.next
                    c.next=a.next
                    if c.next:
                        c.next.back=c
                    del a
                    return
                print("x is last")  
                return
            c=c.next
        print("not found") 
    def Del_before(self,x):
            if self.head is None:
                print("error 0")
                return
            if self.head.Data == x:
                print("error 1")
                return
            c=self.head
            while c:
                if c.Data == x:
                    a=c.back
                    c.back=a.back
                    if c.back:
                        a.back.next=c
                    else:
                        self.head =c
                    del a
                    return
                c=c.next
            print("not found") 
    def Del_x(self,x) :
        if self.head is None:
            print("error 0")
            return
        if self.head.Data == x:
            self.Del_first()
            return
        c=self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.Del_last()
                    return
                c.back.next =c.next
                c.next.back = c.back
                del c
                return
            c=c.next
        print('not found')    
    def Del_all(self):
        while self.head :
            self.Del_first()