def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference

    mini = arr[0]
    maxi = arr[n - 1]

    for i in range(1, n):
        mini = min(arr[0] + k, arr[i] - k) 

        # Minimum element when we add k to whole array
        # Maximum element when we
        maxi = max(arr[i - 1] + k, arr[n - 1] - k)
        
        # subtract k from whole array
        ans = min(ans, maxi - mini)

    return ans

# Driver Code Starts
# arr=[]
# k=int(input("Enter k value to by which number differ: "))
# n=int(input("Enter number of elements:"))
# print("Enter elements:")
# for i in range(n):
#     arr.append(int(input()))
# print("Given array is : ",arr)

arr=[3, 4, 1, 9, 56, 7, 9, 12]
n=len(arr)
k=5
ans = getMinDiff(arr, n, k)
print(ans)