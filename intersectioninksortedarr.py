

# for
def intersection(a,n,b,m,c,l):
    for i in range(n):
        for j in range(m):
            for k in range(l):
                if (a[i] == b[j]) and (b[j] == c[k]):
                    print(f"Intersection is : ",a[i])


# while
# def intersection(a,n,b,m,c,l):
#     i,j,k=0,0,0
#     while(i<n and j<m and k<l):
#         if(a[i]==b[j] and b[j]==c[k]):
#             print(a[i])
#             i+=1
#             j+=1
#             k+=1
#         elif a[i]<b[j]:
#             i+=1
#         elif b[j]<c[k]:
#             j+=1
#         else:
#             k+=1

a=[1,5,10,20,40,80]
a.sort()
n=len(a)
b=[6,7,20,80,100]
b.sort()
m=len(b)
c=[3,4,15,20,30,70,80,120]
c.sort()
l=len(c)
intersection(a,n,b,m,c,l)





