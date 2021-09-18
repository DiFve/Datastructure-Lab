class Queue:
    queue=[]
    def __init__(self):
        self.queue=[]
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

inp = input("Enter Input : ").split(",")
q = Queue()
for i in inp:
    x = i
    if(x[0]=='E'):
        q.append(x[2:])
        print(q.qlen())
    elif(x[0]=='D'):
        if(not(q.isEmpty())):
            print(q.top(),end=" ")
            q.pop()
            print('0')
        else:
            print("-1")
if(not q.isEmpty()):
    lst = q.getQueue()
    for i in lst:
        print(i,end=" ")
else:
    print("Empty")