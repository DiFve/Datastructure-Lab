def mod_position(arr, s):
    word=[]
    for i in range(len(arr)):
        if((i+1)%s==0):
            word.append(arr[i])
    print(word)


print("*** Mod Position ***")
word,x = input("Enter Input : ").split(",")
mod_position(word,int(x))