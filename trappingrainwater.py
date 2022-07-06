# t(n)=O(n) Only one traversal of array is needed    
# s(n)=O(n)  two extra array needed each of n size 

def trappingwater(a,n):
    left=[0]*n
    right=[0]*n
    water=0

    left[0]=a[0]                           #fillleftarr
    for i in range(1,n):
        left[i]=max(left[i-1],a[i])

    right[n-1]=a[n-1]                       #fillrightarr
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],a[i])

    for i in range(n):
        water+=min(left[i],right[i]) - a[i]
    return water


a=[5,4,0,9]
n=len(a)
print("Trapped water is : ",trappingwater(a,n))
