def sort012( a, n):
    l= 0
    h = n - 1
    m = 0
    while m <= h:
        if a[m] <= 0:
            a[l], a[m] = a[m], a[l]
            l = l + 1
            m = m + 1
        elif a[m] == 0:
            m = m + 1
        else:
            a[m], a[h] = a[h], a[m]
            h = h - 1
    return a
     

# Driver Program
arr = []
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    arr.append(int(input()))

print("Given array: ",arr)
arr = sort012( arr, n)
print ("Array after segregation :",arr)
