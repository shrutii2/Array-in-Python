# Time Complexity: O((n+m) Log (n+m))   = O(nlogn)
# Space Complexity: O(n+m). Since we are creating a new array of size n+m. = O(n)

def median(a,n):
    if n%2==0:
        z=n//2
        r=a[z]
        l=a[z-1]
        ans=(l+r)/2
        return ans
    else:
        z=n//2
        ans=a[z]
        return ans

a1=[ 2, 3, 5, 8]
a2=[10, 12, 14, 16, 18, 20]
a=a1+a2
a.sort()
print("Median =",median(a,len(a)))


##t(n)=O(n+m) s(n)=O(1)
# def getMedian(ar1, ar2, n, m) :
#     i = 0 # Current index of input array ar1[]
#     j = 0 # Current index of input array ar2[]
#     m1, m2 = -1, -1
#     if((m + n) % 2 == 1) :   
#         for count in range(((n + m) // 2) + 1) :       
#             if(i != n and j != m) :           
#                 if ar1[i] > ar2[j] :
#                     m1 = ar2[j]
#                     j += 1
#                 else :
#                     m1 = ar1[i]
#                     i += 1           
#             elif(i < n) :           
#                 m1 = ar1[i]
#                 i += 1
#             else :           
#                 m1 = ar2[j]
#                 j += 1       
#         return m1
#     else :
#         for count in range(((n + m) // 2) + 1) :        
#             m2 = m1
#             if(i != n and j != m) :       
#                 if ar1[i] > ar2[j] :
#                     m1 = ar2[j]
#                     j += 1
#                 else :
#                     m1 = ar1[i]
#                     i += 1           
#             elif(i < n) :           
#                 m1 = ar1[i]
#                 i += 1
#             else :           
#                 m1 = ar2[j]
#                 j += 1       
#         return (m1 + m2)//2
 
# # Driver code     
# ar1 = [900]
# ar2 = [5, 8, 10, 20]
 
# n1 = len(ar1)
# n2 = len(ar2)
# print(getMedian(ar1, ar2, n1, n2))