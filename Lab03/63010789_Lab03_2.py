inp = input("Enter expresion : ")
stack=[]
check=0
for i in inp:
    if i=='[' or i=='(' or i=='{':
        stack.append(i)
    if(len(stack)>0):
        if(i==']' and stack[-1]=='['):
            stack.pop(-1)
        elif(i=='}' and stack[-1]=='{'):
            stack.pop(-1)
        elif(i==')' and stack[-1]=='('):
            stack.pop(-1)
        elif((i==')' and stack[-1]=='{')or(i==')' and stack[-1]=='[') or (i=='}' and stack[-1]=='(') or (i=='}' and stack[-1]==']') or (i==']' and stack[-1]=='(') or (i==']' and stack[-1]=='{')):
            check=1
    elif((i==']' or i=='}' or i==')') and len(stack)==0):
        check=2
if(check==1):
    print(inp+" Unmatch open-close")
    exit(0)
if(check==2):
    print(inp+" close paren excess")
    exit(0)
if(len(stack)>0):
    print(inp+" open paren excess   "+str(len(stack))+" : ",end="")
    for i in stack:
        print(i,end="")
    exit(0)
print(inp+" MATCH")

    