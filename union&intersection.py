# T(n)=O(m+n)


def union(a,n,b,m):
    s=set()
    for i in range(n):
        s.add(a[i])
    for i in range(m):
        s.add(b[i])
    print("Number of elements after union operation : ",len(s)," ")
    print("Union set of both array : " + ' ')
    print(s,end=' ')


def intersection(a,n,b,m):
    for i in range(n):
        for j in range(m):
            if (a[i]==b[j]):
                print("\nIntersection is : ",a[i])



#Driver code
a = []
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    a.append(int(input()))

print("Given array: ",a)

b = []
m=int(input("Enter number of another elements: "))
print("Enter elements: ")
for i in range(0,m):
    b.append(int(input()))

print("Given array: ",b)

union(a,n,b,m)
intersection(a,n,b,m)




'''def printUnion(a , n,  b , m):
    mp = {}
     
    # Inserting array elements in mp
    for i in range(n):
        mp[a[i]] = i
 
    for i in range(m):
        mp[b[i]] = i
     
    print("The union set of both arrays is : ");
    for key in mp.keys():
 
        print(key,end=" ")'''

# def intersection(a,n,b,m):
#     p=0
#     q=0
#     intersect = []
    
#     while p< n and q<m:
#         if a[p]==b[q]:
#             if p==0 or a[p] != a[p-1]:
#                 intersect.append(a[p])
#                 p+=1
#                 q+=1
#             elif a[p] < b[q]:
#                 p+=1
#             else:
#                 q+=1
#     return intersect






