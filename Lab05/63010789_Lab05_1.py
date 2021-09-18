class LinkedList :    
    class Node :           
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):    
        if len(self)==0:
            return "Empty"
        s=""
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
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
            return "Found "+data+" in "+str(self)
        else:
            return "Not Found "+data+" in "+str(self)
            
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
          self.size += 1
        else :                        
          self.insertAfter(len(self)-1,data) 
    
    def insertAfter(self,i,data) :      
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
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
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1
    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0}".format(L.search(i[3:])))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(len(L), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.indexOf(i[3:]), L))
    elif i[:2] == "PO":
        before = str(L)+""
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)