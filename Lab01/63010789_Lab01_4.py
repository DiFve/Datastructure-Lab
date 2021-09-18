print("*** Fun with Drawing ***")
n = int(input("Enter input : "))

for i in range(n):
    print("."*(n-i-1),end="")
    print("*",end="")
    print("+"*((2*i)-1),end="")
    if(i!=0):
        print("*",end="")
    print("."*((2*(n-i-1))-1),end="")
    if(i!=n-1):
        print("*",end="")
    print("+"*((2*i)-1),end="")
    if(i!=0):
        print("*",end="")
    print("."*(n-i-1))
for i in range(n+n-2):
    print("."*(i+1),end="")
    print("*",end="")
    print("+"*((n+n-3-i)),end="")
    print("+"*((n+n-4-i)),end="")
    if(i!=n+n-3):
        print("*",end="")
    print("."*(i+1))