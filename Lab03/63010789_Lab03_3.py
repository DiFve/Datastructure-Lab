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
            return "err"
    def append(self,num):
        self.stack.append(num)
    def __str__(self):
        return str(self.stack)
    def stklen(self):
        return int(len(self.stack))
    def getStack(self):
        return self.stack
    def setStack(self,stk):
        self.stack = stk


inp=input("Enter Infix : ")
s = Stack()
dic = { "^":3, 
        "*":2,
        "/":2,
        "+":1,
        "-":1,
        "(":0,
        "err":-1}
print("Postfix : ",end="")
for i in inp:
    if i.isalpha():
        print(i,end="")
    else:
        if(s.stklen()==0 or i=='('):
            s.append(i)
        elif(i==')'):
            while(s.top()!='('):
                print(s.top(),end="")
                s.pop()
            s.pop()
        elif(dic[i]>dic[s.top()]):
            s.append(i)
        elif(dic[i]<=dic[s.top()]):
            while(dic[i]<=dic[s.top()]):
                print(s.top(),end="")
                s.pop()
            s.append(i)
for i in range(s.stklen()):
    print(s.top(),end="")
    s.pop()
