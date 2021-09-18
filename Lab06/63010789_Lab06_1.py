def fact(x):
    x = int(x)
    if x==1 or x==0:
        return 1
    else:
        x*=fact(x-1)
        return x

inp = input("Enter Number : ")
print(str(inp)+"! = "+str(fact(inp)))