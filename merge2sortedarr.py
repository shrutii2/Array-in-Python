


# def mergeArray(a,n,b,m): O(n+m) for t and s
    # p=[None]*(n + m)
    # i=0
    # j=0
    # k=0
    # while i<n and j<m:
    #     if a[i]<b[j]:
    #         p[k]=a[i]
    #         k+=1
    #         i+=1
    #     else:
    #         p[k]=b[j]
    #         k+=1
    #         j+=1
    # while i<n:
    #     p[k]=a[i]
    #     k+=1
    #     i+=1
    # while j<m:
    #     p[k]=b[j]
    #     k+=1
    #     j+=1
    # print("After merging:")
    # for i in range(n+m):
    #     print(str(p[i]),end=' ')


a = []
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    a.append(int(input()))
print("Given array: ",a)
b = []
m=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,m):
    b.append(int(input()))
print("Given array: ",b)
# mergeArray(a,n,b,m)``
 
#option1:
a.sort()
b.sort()
print("Merged two array is :",a+b)