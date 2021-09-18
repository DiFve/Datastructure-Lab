class Queue:
    queue=[]
    maxq=0
    def __init__(self,max):
        self.queue=[]
        self.maxq=max
    def pop(self):
        if(len(self.queue)>0):
            self.queue.pop(0)
    def top(self):
        if(len(self.queue)>0):
            return self.queue[0]   
        else:
            return "err"
    def append(self,num):
        self.queue.append(num)
    def __str__(self):
        return str(self.queue)
    def qlen(self):
        return int(len(self.queue))
    def getQueue(self):
        return self.queue
    def setQueue(self,q):
        self.queue = q
    def isEmpty(self):
        if(len(self.queue)>0):
            return False
        else:
            return True
    def isFull(self):
        if(len(self.queue)<self.maxq):
            return False
        else:
            return True



inp = input("Enter people : ")
mainQ = list(inp)
q1=Queue(5)
q2=Queue(5)
count=1
timer1,timer2=0,0

for i in inp:
    mainQ.pop(0)
    print(count,end=" ")
    print(mainQ,end=" ")
    if(timer1>=3):
        q1.pop()
        timer1=0
    if(timer2>=2):
        q2.pop()
        timer2=0
    
    if(not q1.isFull()):
        q1.append(i)
    elif(not q2.isFull()):
        q2.append(i)

    if(not q1.isEmpty()):
        timer1+=1
    if(not q2.isEmpty()):
        timer2+=1
    lst1=q1.getQueue()
    lst2=q2.getQueue()
    print(lst1,end=" ")
    print(lst2)
    
    count+=1
    

    