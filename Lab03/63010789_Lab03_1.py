inp = input("Enter Input : ").split(",")
stack = []
stackSize=0
for i in inp:
    temp = i
    if(temp[0]=='A'):
        stackSize+=1
        print("Add = "+temp[2:]+" and Size = "+str(stackSize))
        stack.append(temp[2:])
    elif(temp[0]=='P'):
        if(stackSize>0):
            stackSize-=1
            print("Pop = "+stack[-1]+" and Index = "+str(stackSize))
            stack.pop(-1)
        else:
            print("-1")

if(stackSize>0):
    print("Value in Stack = ",end="")
    for i in stack:
        print(i,end=" ")
else:
    print("Value in Stack = Empty")