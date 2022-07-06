

def palindrome(n):                  #for checking palindrome
    str1=''+str(n)
    len1=len(str1)
    for i in range(len1//2):
        if str1[i] != str1[len1- 1- i]:
            return False
    return True

def ispalinarr(a,n):                  #for checking if array is palindrome array
    for i in range(n):
        ans=palindrome(a[i])
        if ans==False:
            return False
        return True


a=[121,161,111]
n=len(a)
res=ispalinarr(a,n)
if res==True:
    print("Array is palinarray")
else:
    print("Array is not palindromearray.")