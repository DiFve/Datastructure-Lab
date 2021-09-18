def dec2bin(x):
    x = int(x)
    s = ""
    if x == 0:
        return "0"
    if x>1:

        reminder = x%2
        x/=2
        # print("reminder"+str(reminder))
        
        s+=dec2bin(x)
        s+=str(reminder)
        
    else:
        reminder = 1
        return str(reminder)
    return str(s)


def findAllnum(x,maxdigit):
    x = int(x)
    maxdigit = int(maxdigit)
    if maxdigit<0:
        print("Only Positive & Zero Number ! ! !")
        return 0
    if x==0:
        s = dec2bin(x)
        if len(s)<maxdigit:
            temp = "0"*(maxdigit-len(s))
            s = temp+s
        print(s)
    else:
        
        findAllnum(x-1,maxdigit)
        s = dec2bin(x)
        if len(s)<maxdigit:
            temp = "0"*(maxdigit-len(s))
            s = temp+s
        print(s)

inp = input("Enter Number : ")
inp = int(inp)
findAllnum((2**inp)-1,inp)
