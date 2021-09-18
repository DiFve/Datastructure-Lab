def pyramid(x,i):
    x = int(x)
    f="_"
    b="#" 
    if x>0 and i<x+1:
        f*=(x-i)
        b*=i
        print(f+b)
        pyramid(x,i+1)
    elif x<0 and i<(-x+1):
        x = -x
        f*=i-1
        b*=(x-i)+1
        print(f+b)
        pyramid(-x,i+1)
    elif x==0:
        print("Not Draw!")
        

inp = input("Enter Input : ")
pyramid(inp,1)