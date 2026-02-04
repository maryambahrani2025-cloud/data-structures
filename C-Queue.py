class c_Queue:
    def __init__(self,limit):
        self.list=[]*limit
        self.front=-1
        self.rear=-1
        self.limit=limit
    def insert(self,x):
        if (self.rear+1)%self.limit== self.front:
            print("Queue is full")  
            return
        if self.front==-1:
            self.front=0
            self.rear=0
            self.list[0]=x
            return
        self.rear=self.rear+1 % self.limit
        self.list[self.rear]=x
    def delete(self):
        if self.rear== -1:
            print("Queue is empty")
            return
        if self.rear == self.front:
            k=self.list[self.front]
            self.front=-1
            self.rear=-1
            return k
        k=self.list[self.front]
        self.front+=1
        return k
    def is_full(self):
        return self.rear+1 % self.limit == self.front
    def is_empty(self):
        return self.front == -1
    def show_valid (self):
        if self.rear>= self.front:
            for i in range(self.front,self.rear+1,1):
                print(self.list[i])
        else:
            for i in range(0,self.rear+1,1) :
                print(self.list[i])     
    def show_invalid(self):
        pass
    def find(self,x):
        pass
    def replace(self,x,y):
        pass
    