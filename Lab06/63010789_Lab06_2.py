def isPalindrome(word,indexStart,indexEnd):
    # print(word[indexStart]+"=="+word[indexEnd])
    if len(word)==1 or len(word)==0:
        return True
    if word[indexStart] == word[indexEnd]:
        word = word[1:-1]
        return isPalindrome(word,0,-1)
    else:
        return False
    


inp = input("Enter Input : ")
if isPalindrome(inp,0,-1):
    print("'"+inp+"' is palindrome")
else:
    print("'"+inp+"' is not palindrome")
