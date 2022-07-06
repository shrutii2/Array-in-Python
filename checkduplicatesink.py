def checkDuplicatesWithinK(arr, n, k):
    myset = []
    for i in range(n):
        if arr[i] in myset:
            return True
        myset.append(arr[i])

        if (i >= k):
            myset.remove(arr[i - k])
    return False

a = []
k=int(input("Enter k:"))
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    a.append(int(input()))
print("Given array: ",a)
if (checkDuplicatesWithinK(a,n,k)):
    print("YES")
else:
    print("NO")