def sumList(arr):
    ans=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if(arr[i]+arr[j]+arr[k]==0):
                    temp = [arr[i],arr[j],arr[k]]
                    if temp not in ans:
                        ans.append(temp)
    print(ans)


inp = [int(x) for x in input("Enter Your List : ").split()]
if(len(inp)<3):
    print("Array Input Length Must More Than 2")
else:
    sumList(inp)