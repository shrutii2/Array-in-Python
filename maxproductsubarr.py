

def maxSubarrayProduct(a,n):
    m=a[0]
    # st=0
    # end=0
    # pos=0
    for i in range(n):
        mul=a[i]
        for j in range(i+1,n):
            m=max(m,mul)
            mul*=a[j]
            # st=pos
            # end=i
        m=max(m,mul)
    
    print("Max product subarray is",m)
    # print("Start index of window is",st,"and end index is",end)


n=5
a=[-1,-3,-10,0,60]
maxSubarrayProduct(a,n)


def minProdK(arr, K):
    prod = 1
    zeros = 0
    N = len(arr)
    for i in range(K):
        if (arr[i] == 0):
            zeros += 1
        else:
            prod *= arr[i]
    if zeros == 0:
        res = prod
    else:
        res = 0
    for right in range(K,  N):
        if (arr[right] == 0):
            zeros += 1
        else:
            prod *= arr[right]
        if (arr[right - K] == 0):
            zeros -= 1
        else:
            prod //= arr[right - K]
        if (zeros == 0):
            res = min(res, prod)
        elif (res > 0):
            res = 0
    return res
 
# Driver code

arr = [2, 3, -1, -5, 4, 0]
K = 3
print(minProdK(arr, K))