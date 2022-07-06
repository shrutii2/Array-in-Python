# t(N)=O(n^2)   s=O(1)
# for 2 numbers:
# def findpair(a,n,sum):
#     for i in range(n):
#         for j in range(i+1,n):
#             if (a[i]+a[j]==sum):
#                 print("(",a[i],",",a[j],")")

# t(n)=O(n)   s=O(1)
def findpair(a,n,s):
    a.sort()
    for i in range(n):
        l=i
        r=n-1
        while(l<r):
            if a[l]+a[r]==s:
                print("(",a[l],",",a[r],")")
                return True
            elif a[l]+a[r]<s:
                l+=1
            else:
                r-=1
    return False

a=[1, 4, 45, 6, 10, 8]
n=len(a)
findpair(a,n,14)

#t=O(n^3) s=O(1)
# def findtriplet(a,n,sum):
#     for i in range(0,n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 if a[i]+a[j]+a[k]==sum:
#                     print("Triplet is", a[i],", ", a[j], ", ", a[k])
#                     return True
#     return False

# t(n)=O(n^2)    s=O(1)
# def findtriplet(a,n,s):
#     a.sort()
#     for i in range(0,n-2):
#         l=i+1
#         r=n-1
#         while (l<r):
#             if a[i]+a[l]+a[r]==s:
#                 print("Triplet is", a[i],", ", a[l], ", ", a[r])
#                 return True
#             elif a[i]+a[l]+a[r]<s:
#                 l+=1
#             else:
#                 r-=1
#     return False


# a=[1, 4, 45, 6, 10, 8]
# n=len(a)
# findtriplet(a,n,22)
