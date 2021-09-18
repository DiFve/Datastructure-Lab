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
        i=0
        if len(self.queue)==0:
            self.queue.append(num)
        else:
            while(i<len(self.queue)):
                if(int(num[0])!=int(self.queue[i][0])):
                    i+=1
                    continue
                else:
                    j=i
                    while(int(num[0])==int(self.queue[j][0])):
                        j+=1
                        if(j>=len(self.queue)-1):
                            break
                    self.queue.insert(j,num)
                    return 0
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

Qwait = Queue()
inpLeft,inpRight = input("Enter Input : ").split("/")
left = inpLeft.split(",")
right = inpRight.split(",")

dic = {}

for i in left:
    dic[int(i[2:])]=i
# print(dic)
# for i in dic.values():
#     print(i)



for i in right:
    if(i[0]=='D'):
        if(Qwait.isEmpty()):
            print("Empty")
        else:
            print(Qwait.top()[2:])
            Qwait.pop()
    elif(i[0]=='E'):
        Qwait.append(dic[int(i[2:])])
        # print(Qwait)




