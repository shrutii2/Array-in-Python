





# option1 : simple t=O(n^2) and s=O(1)
def countInversion(a,n):
    
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                print("Inversion pair is:\n[",a[i],",",a[j],"]")
                count+=1           
    return count


# option2:mergesort t=O(nlogn) s=O(n)

# def mergeSort(arr, n):
#     temp_arr = [0]*n
#     return _mergeSort(arr, temp_arr,0, n - 1)

# def _mergeSort(arr, temp_arr, left, right):
#     inv_count = 0
#     if left < right:
#         mid = (left + right)
#         inv_count += _mergeSort(arr, temp_arr,left, mid)
#         inv_count += _mergeSort(arr, temp_arr,mid + 1, right)
#         inv_count += merge(arr, temp_arr,left, mid, right)
#     return inv_count

# def merge(arr, temp_arr, left, mid, right):
#     i = left     
#     j = mid + 1 
#     k = left     
#     inv_count = 0
#     while i <= mid and j <= right:
#         if arr[i] <= arr[j]:
#             temp_arr[k] = arr[i]
#             k += 1
#             i += 1
#         else:
#             temp_arr[k] = arr[j]
#             inv_count += (mid-i + 1)
#             k += 1
#             j += 1
    
#     while i <= mid:
#         temp_arr[k] = arr[i]
#         k += 1
#         i += 1
#     while j <= right:
#         temp_arr[k] = arr[j]
#         k += 1
#         j += 1

#     for loop_var in range(left, right + 1):
#         arr[loop_var] = temp_arr[loop_var]

#     return inv_count


a = []
n=int(input("Enter elements count:"))
print('Enter elements:')
for i in range(0,n):
    a.append(int(input()))
print("Given array: ",a)

# resul=countInversion(a,n)
print("Inversion count is:",countInversion(a,n))