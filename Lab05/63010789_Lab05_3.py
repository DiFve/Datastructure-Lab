class LinkedList :    
    class Node :           
        def __init__(self, data) :
            self.data = data
            self.next = None
            self.previous = None
        
    def __init__(self):                
            self.head = None
            self.tail = None
            self.size = 0
            
    def __str__(self):    
        if len(self)==0:
            return "Empty"
        s=""
        p = self.head
        while p != None :
            s += str(p.data) + " " 
            p = p.next
        return s

    def reverse(self):
        if len(self)==0:
            return "Empty"
        s=""
        p = self.tail
        while p!=None:
            s += str(p.data) + " " 
            p = p.previous
        return s


    def __len__(self) :    
        return self.size         
            
    
    def isEmpty(self) :       
        return self.size == 0
        
    def indexOf(self,data) :       
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
    
    def search(self,data):
        if (self.indexOf(data)!=-1):
            return "Found "
        else:
            return "Not Found "
            
    def isIn(self,data) :         
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :          
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def append(self,data):           
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.tail = p
          self.next = None
          self.previous = None
          self.size += 1
        else :                        
          self.insertAfter(len(self)-1,data) 
    
    def insertAfter(self,i,data) :
        if len(self)==0:
            self.addHead(data)   
        else:
            if i<0:
                if(-i>len(self)):
                    i=-1
                else:
                    i=len(self)+i-1
            if i>=len(self):
                i=len(self)-1
            if i==-1:
                self.addHead(data)
            else:
                q = self.nodeAt(i)
                p = self.Node(data)
                if len(self)-1!=i:
                    r = self.nodeAt(i+1)
                    r.previous = p

                p.next = q.next
                q.next = p
                p.previous = q
                
                if i==len(self)-1:
                    self.tail = p
                self.size += 1
    
    def deleteAfter(self,i) :           
        if len(self) > 0 :  
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1
    
    def pop(self,i) :                 
        if len(self)>0 and i<len(self):
            if i == 0 and len(self) > 0 :    
                self.head = self.head.next
                self.size -= 1
            else :
                self.deleteAfter(i-1)          
            return "Success"
        else:
            return "Out of Range"
        

    def removeData(self,data) :          
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
            p = self.Node(data)
            self.head = p
            self.tail = p
            self.size += 1
        else :
            q=self.head
            p = self.Node(data)
            q.previous = p
            p.next = q
            self.head = p
            self.size += 1
    
inp = input("Enter Input (L1,L2) : ").split(" ")
L1 = inp[0].split("->")
L2 = inp[1].split("->")

LL1 = LinkedList()
LL2 = LinkedList()

for i in L1:
    LL1.append(i)
for i in L2:
    LL2.addHead(i)
mergeList = LinkedList()
for i in range(len(LL1)):
    mergeList.append(LL1.nodeAt(i).data)
for i in range(len(LL2)):
    mergeList.append(LL2.nodeAt(i).data)
print("L1    : "+str(LL1))
print("L2    : "+str(LL2.reverse()))
print("Merge : "+str(mergeList))

