
# n=int(input('n='))
arr=[1, 2, 3, 4, 5]
d=int(input('d='))
# print("Enter array: ")

arr=arr[d:]+arr[:d]
print(*arr)



'''ip:
5 4
1 2 3 4 5
op:
5 1 2 3 4'''