# # T(n)=O(n)    S(n)=O(1)

# # slidingwindowapproach

def minSwap(arr, n, k) :
    count = 0
    for i in range(0, n) :
        if (arr[i] <= k) :
            count = count + 1
    large_count=0
    for i in range(0, count) :
        if (arr[i] > k) :
            large_count = large_count + 1
    ans = large_count
    j = count
    for i in range(0, n) :
        if(j == n) :
            break
        if (arr[i] > k) :
            large_count = large_count - 1
        if (arr[j] > k) :
            large_count = large_count + 1
        ans = min(ans, large_count)
        j = j + 1
    return ans

# Driver code
arr1 = [2, 7, 9, 5, 8, 7, 4]
n = len(arr1)
k = 5
print (minSwap(arr1, n, k))
 
