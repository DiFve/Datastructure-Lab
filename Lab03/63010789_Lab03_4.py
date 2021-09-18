class Stack:
    stack=[]
    def __init__(self):
        self.stack=[]
    def pop(self):
        if(len(self.stack)>0):
            self.stack.pop()
    def top(self):
        if(len(self.stack)>0):
            return self.stack[-1]   
        else:
            return -9999
    def append(self,num):
        self.stack.append(num)
    def __str__(self):
        return str(self.stack)
    def stklen(self):
        return int(len(self.stack))

inp = input('Enter Input : ').split(',')
s1 = Stack()
s2 = Stack()
for i in inp:
    lst = i
    if(i[0]=='A'):
        s1.append(int(i[2:]))
    elif(i[0]=='B'):
        if(s1.stklen()>0):
            count=1
            temp=s1.top()
            s2.append(s1.top())
            s1.pop()
            for j in range(s1.stklen()):
                if(temp<s1.top()):
                    temp=s1.top()
                    count+=1
                s2.append(s1.top())
                s1.pop()
            if(s1.stklen()==0):
                print(count)    
                
            for j in range(s2.stklen()):
                s1.append(s2.top())
                s2.pop()
            # print("1:"+str(s1))
        else:
            print("0")
    
            
