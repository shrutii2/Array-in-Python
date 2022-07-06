# T=O(N)   s=O(1)

# for alternate -ve and +ve
def rearrange(arr):
    p = 0
    b = 0
    for i in range(len(arr)):
        if b == 1:
            b -= 1
        elif arr[i] < 0:
            arr[i], arr[p] = arr[p], arr[i]
            if p > i:
                b += 1
            p += 2
    return arr


array = [-5,-2,5,2,4,7,1,8,0,-8]
print("After Rearranging :", rearrange(array))

# for alternate smallest and largest: t =O(n) s=O(n)
# def rearrange(a,n):
#     temp=n*[None]
#     s,l=0,n-1
#     flag=True
#     for i in range(n):
#         if flag == True:
#             temp[i]=a[l]
#             l-=1
#         else:
#             temp[i]=a[s]
#             s+=1
#         flag=bool(1-flag)
#     for i in range(n):
#         a[i]=temp[i]
#     return a

# arr = [1, 2, 3, 4, 5, 6]
# n = len(arr)
# print("Original Array")
# print(arr)
# print("Modified Array")
# print(rearrange(arr, n))
