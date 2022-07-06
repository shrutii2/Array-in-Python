# t(n)=O(n)        s(n)=O(1)

from sys import maxsize

def smallestSubarrwithSum(a,n,x):
    curr_sum=0
    length= maxsize
    start=0
    for end in range(n):
        curr_sum+=a[end]
        while curr_sum>x and start<=end:
            length=min(length,end-start+1)
            curr_sum-=a[start]
            start+=1

    if length==maxsize:
        return 0
    return length

a=[1, 10, 5, 2, 7]
n=len(a)
x=9
result=smallestSubarrwithSum(a,n,x)
print("Not possible") if (result==n+1) else print(result)