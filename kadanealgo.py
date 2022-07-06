# # # T(N) = O(N) S(N) = O(1)
# # Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


def maxSubarraySum(a,n):
    m=a[0]
    c=0
    st=0
    end=0
    pos=0
    for i in range(n):
        c=c+a[i]
        if(m<c):
            m=c
            st=pos
            end=i
        if(c<0):
            c=0
            pos=i+1
    print("Max sum subarray is",m)
    print("Start index of window is",st,"and end index is",end)




a=[]
n=int(input("Enter number of elements:"))
print("Enter elements:")
for i in range(n):
    a.append(int(input()))
print("Given array is : ",a)
maxSubarraySum(a,n)










# '''def maxSubarraySum(a,n):  this is not kadane algo but it is right
#     s=[]
#     m=int(input("Enter elements from given set whose we wnat max sum: "))
#     print("Enter elements: ")
#     for i in range(m):
#         s.append(int(input()))
#     print(s)
#     p=len(s)
#     print("Maximum from given set",max(a),"and from input set",max(s))
#     h=0
#     for i in range(0,p):
#         h=h+s[i]
#     print("Sum of input subarray is :",h)'''




# def maxSubarraySum(a,n):
#     ma=a[0]
#     sum=0
#     for i in range(0,n):
#         sum=sum+a[i]
#         if (sum > ma):
#             ma=sum
#         if (sum < 0):
#             sum=0



# a=[3,2,5,-4,7,5,2]
# n=len(a)
# maxSubarraySum(a,len(a))



