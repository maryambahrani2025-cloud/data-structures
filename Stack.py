class stack:
    def __init__ (self,limit=10):
        self.list=[]
        self.limit=limit
    def push(self,x):
        if len(self.list)>= self.limit:
            print("stack is full")    
            return-1
        self.list .append(x)
    def pop(self):
        if len(self.list)== 0:
            print("stack is empty")
            return -1
        return self.list .pop()
    def peek(self):
        if len(self.list)== 0:
            print("stack is empty")
            return -1
        return self.list[-1]
    def find(self,x):
        for i in range(len(self.list)):
            if self.list[i]==x:
                print(i)
    def find2(self,x):
        for i in range(len(self.list)):
            if self.list[i]==x:
               print (i)       
               return
    def find3(self,x):
        for i in range(len(self.list),-1,-1,-1):
            if self.list[i]==x:
                print(i)  
                return
    def find4(self,x):
        for i in range(len(self.list),-1,-1,-1):
            if self.list[i]==x:
                p=i
            print(p)  
    def find5(self,x):
        list=[]   
        for i in range(len(self.list)):
            if self.list[i] == x:
                list.append(i)      
            print(list[3])    
    def replace(self,x,y):
        for i in range(len(self.list)):
            if self.list[i]==x:
                self.list[i]=y
    def replace2(self,x,y,n):
        list=[]
        for i in range(len(self.list)):
            if self.list[i]==x:
                list.append(i)
        for j in range (len(list)) :
            if j== n:
                self.list[list[j]] == y
test= stack()
test.push(15) 
test.push(12) 
test.push(11) 
test.push(1)  
test.find(12)          
                           
                                        