class node :
    def __init__(self,data):
        self.Data= data
        self.next= None
class linked_list:
    def __init__(self):
        self.head = None
    def insert_first(self,x):
        if self.head is None :
            self.head=node(x)
            return
        a=node(x)
        a.next=self.head
        self.head=a
    def insert_last(self,x) :
        if self.head is None:
            self.head = node(x)
            return
        a=node(x)
        c=self.head
        while c.next:
            c=c.next
        c.next=a
    def insert_after(self,x,y) :
        if self.head is None:
            print("list is empty")
            return
        c=self.head
        while c:
            if c.Data == x:
                a=node(y)
                a.next=c.next
                c.next=a
                return
            c=c.next
        print("not found")
    def  insert_before(self,x,y):
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.insert_first(y)
            return
        c=self.head
        while c.next:
            if c.next.Data == x :
                a=node(y)
                a.next = c.next
                c.next=a
                return
            c=c.next
        print("not found") 
    def Del_first(self)  :
        if self.head is None:
            print ("list is empty")
            return
        c=self.head
        self.head=c.next
        del c
    def Del_last(self) :
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.Del_first()
            return
        c=self.head
        while c.next.next :
            c=c.next
        del c.next
        c.next=None
    def Del_after(self,x):
        if self.head is None:
            print("list is empty") 
            return
        if self.head.next is None:
            print("error 1")  
            return
        if self.head.Data == x:
            a=self.head.next
            self.head=a.next
            del a
            return
        c=self.head
        while c.next:
            if c.Data == x:
                a=c.next
                c.next=a.next
                del a
                return
            c=c.next
        print ("not found")  
    def Del_before(self,x) :
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            print("error 1")
            return
        if self.head.next == x:
            print ("error x1")
            return
        if self.head.next.Data == x :
            self.Del_first()
            return
        if self.head.next.next is None:
            print("error 2")
            return
        c=self.head
        while c.next.next :
            if c.next.next.Data == x:
                a=c.next
                c.next=a.next
                del a
                return
            c=c.next
        print("not found")   
    def Del_x(self,x) :
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.Del_first()
            return
        c=self.head
        while c.next :
            if c.next.Data == x:
                a=c.next
                c.next = a.next
                del a
                return
            c=c.next
        print("not found")
    def Del_all(self) :
        while self.head:
            self.Del_first()