class Queue:
    def __init__(self,limit):
        self.list=[]*limit
        self.limit=limit
        self.front=-1
        self.rear=-1
    def insert(self,x):
        if self.rear>=len(self.list):
            print("Queue is full")
            return
        if self.front==-1:
            self.front=0
            self.rear=0
            self.list[0]=x
            return
        self.rear+=1
        self.list[self.rear]=x
    def delete(self):
        if self.rear==-1:
            print("Queue is empty")
        if self.front == self.rear:
            k=self.list[self.front] 
            self.front=-1
            self.rear=-1
            return k
        k=self.list[self.front]
        self.front=-1
        return k 
    def fix(self):
        if self.rear==-1:
            print("Queue is empty") 
            return 
        new_pos=0
        for i in range (self.front,self.rear+1,1):
            self.list[new_pos]=self.list[i]
            new_pos+=1
        for j in range (new_pos,len(self.list)) :
            self.list[j]=None
        self.front=0
        self.rear=new_pos-1       
               