class Stack:
    stack=[]
    maxStack=0
    def __init__(self,max):
        self.stack=[]
        self.maxStack = max
    def pop(self):
        if(len(self.stack)>0):
            self.stack.pop()
    def top(self):
        if(len(self.stack)>0):
            return self.stack[-1]   
        else:
            return -9999
    def append(self,num):
        if(num in self.stack):
            return "car "+str(num)+" already in soi"
        elif(len(self.stack)<self.maxStack):
            self.stack.append(num)
            return "car "+str(num)+" arrive! : Add Car "+str(num)
        else:
            return "car "+str(num)+" cannot arrive : Soi Full "
    def __str__(self):
        return self.stack
    def stklen(self):
        return int(len(self.stack))
        


print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
allCar = s.split(",")
s1 = Stack(m)
s2 = Stack(m)
if(s != '0'):
    for i in allCar:
        s1.append(int(i))
if(o=="arrive"):
    print(s1.append(n))
elif(o=="depart"):
    lst = s1.__str__()
    if(len(lst)==0):
        print("car "+str(n)+" cannot depart : Soi Empty")
    elif(n not in lst):
        print("car "+str(n)+" cannot depart : Dont Have Car "+str(n))
    else:
        num = s1.stklen()
        for i in range(int(num)):
            if(int(s1.top())!=n):
                s2.append(s1.top())
                s1.pop()
            else:
                s1.pop()
                break
        num2 = s2.stklen()
        for i in range(int(num2)):
            s1.append(s2.top())
            s2.pop()
        print("car "+str(n)+" depart ! : Car "+str(n)+" was remove")
            
print(s1.__str__())