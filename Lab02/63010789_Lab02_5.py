def bon(w):
    check = [0]*26
    for i in w:
        i.lower()
        check[ord(i)-97]+=1
    ans = 0
    for i in range(len(check)):
        if(check[i]>1):
            ans = (i+1)*4
    return str(ans)
        


secretCode = input("Enter secret code : ")
print(bon(secretCode))