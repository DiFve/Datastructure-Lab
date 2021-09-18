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

inp = input("Enter Input (Normal, Mirror) : ").split(" ")
normal = inp[0]
mirror = inp[1]
mirrorItem = []
mirrorCount=0
normalCount = 0
mirrorFailed = 0
i=0

mirror = mirror[::-1]
while(i<=len(mirror)-3):
    if(mirror[i]==mirror[i+1]==mirror[i+2]):
        mirrorItem.append(mirror[i])
        mirror = mirror[0:i]+mirror[i+3:]
        i=0
        mirrorCount+=1
        continue
    i+=1
i=0
while(i<=len(normal)-3):
    if(normal[i]==normal[i+1]==normal[i+2]):
        
        if(len(mirrorItem)!=0):
            normal = normal[0:i+2]+str(mirrorItem.pop(0))+normal[i+2:]
            if(normal[i]==normal[i+1]==normal[i+2]):
                normal = normal[0:i]+normal[i+3:]
                mirrorFailed+=1
                i=0
                continue
        if(normal[i]==normal[i+1]==normal[i+2]):
                normal = normal[0:i]+normal[i+3:]
                normalCount+=1
                i=0
                continue
    i+=1
print("NORMAL :")
print(len(normal))
if(len(normal)!=0):
    print(normal[::-1])
else:
    print("Empty")
print(str(normalCount)+" Explosive(s) ! ! ! (NORMAL)")
if(mirrorFailed!=0):
    print("Failed Interrupted "+str(mirrorFailed)+" Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(len(mirror))
if(len(mirror)!=0):
    print(mirror[::-1])
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE "+str(mirrorCount))

