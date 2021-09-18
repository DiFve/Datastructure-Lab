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
    def isFull(self):
        if(len(self.queue)<self.maxq):
            return False
        else:
            return True

def encodemsg(q1,q2):
    q = Queue()
    lst = []
    count=0
    for i in q1:
        q.append(i)
    for i in range(len(q1)):
        if(q.top().isalpha()):
            x = q.top()
            q.pop()
            x = ord(x)+int(q2[count%len(q2)])
            count+=1
            if(ord(q1[i])<=90 and x>90):
                x-=26
            elif(ord(q1[i])<=122 and x>122):
                x-=26
            lst.append(chr(x))
        else:
            q.pop()
            continue
    return lst

def decodemsg(q1,q2):
    q = Queue()
    lst = []
    count=0
    for i in q1:
        q.append(i)
    for i in range(len(q1)):
        if(q.top().isalpha()):
            x = q.top()
            q.pop()
            x = ord(x)-int(q2[count%len(q2)])
            count+=1
            if(ord(q1[i])>=65 and x<65):
                x+=26
            elif(ord(q1[i])>=97 and x<97):
                x+=26
            lst.append(chr(x))
        else:
            q.pop()
            continue
    return lst

word,key = input("Enter String and Code : ").split(",")
enc = encodemsg(word,key)
print("Encode message is :  "+str(enc))
print("Decode message is :  "+str(decodemsg(enc,key)))
