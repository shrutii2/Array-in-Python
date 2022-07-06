def clwarrayppos(a,n):
    i=0
    while i != n-1:
            a[i],a[n-i-1]=a[n-i-1],a[i]
            i+=1
    return a

a=[]
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
    a.append(int(input()))
print("given array is: ",a)
clwarrayppos(a,n)
print("After clockwise direction: ",a)
