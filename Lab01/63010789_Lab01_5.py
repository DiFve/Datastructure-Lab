print("Enter All Bid : ",end="")
inp = [int(x) for x in input().split()]
inp.sort()
if(len(inp)==1):
    print("not enough bidder")
elif(inp[len(inp)-1] != inp[len(inp)-2]):
    print("winner bid is " +str(inp[len(inp)-1])+ " need to pay " +str(inp[len(inp)-2]))
else:
    print("error : have more than one highest bid")