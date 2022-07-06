'''
Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts. 
1) All elements smaller than lowVal come first. 
2) All elements in range lowVal to highVVal come next. 
3) All elements greater than highVVal appear in the end. 
The individual elements of three sets can appear in any order.

Examples: 
Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
        lowVal = 14, highVal = 20
Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}

'''

# T(n)= O(n) S(n)=O(1)       
# 1 approach is by sorting but its time complexity will be O(nlogn)


def threewaypartitioning(a,n,leftval,rightval):
    start=0
    end=n-1
    i=0
    a.sort()
    while i<=end:
        if a[i]<leftval:
            a[i],a[start]=a[start],a[i]
            i+=1
            start+=1
        elif a[i]>rightval:
            a[i],a[end]=a[end],a[i]
            end-=1
        else:
            i+=1
    return 1


a=[1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
n=len(a)
print(threewaypartitioning(a,n,14,20))

print("Modified Array :")
for i in range (n):
    print(a[i],end=' ')