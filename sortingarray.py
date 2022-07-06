# # T(n) = O(n)    and S(n) = O(1)


# # Function to sort the array of 0s, 1s and 2s  
# def sortArr(arr, n):
#     cnt0 = 0
#     cnt1 = 0
#     cnt2 = 0
    
#     # Count the number of 0s, 1s and 2s in the array
#     for i in range(n):
#         if arr[i] == 0:
#             cnt0+=1
        
#         elif arr[i] == 1:
#             cnt1+=1
    
#         elif arr[i] == 2:
#             cnt2+=1
    
#     # Update the array
#     i = 0
    
#     # Store all the 0s in the beginning
#     while (cnt0 > 0):
#         arr[i] = 0
#         i+=1
#         cnt0-=1
     
#     # Then all the 1s
#     while (cnt1 > 0):
#         arr[i] = 1
#         i+=1
#         cnt1-=1
     
#     # Finally all the 2s
#     while (cnt2 > 0):
#         arr[i] = 2
#         i+=1
#         cnt2-=1
     
#     # # Print the sorted array
#     # printArr(arr, n)
 
 
# # Driver code
 
# # arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# arr=[]
# n = int(input("Enter no. of elements: "))
# print("Enter elements: ")

# for i in range(n):
#     arr.append(int(input()))

# print("Given an array: ",arr)
# sortArr(arr, n)

# print("Sorted array : ",arr)


#option2:

# def sort012( a, n):
#     l= 0
#     h = n - 1
#     m = 0
#     while m <= h:
#         if a[m] == 0:
#             a[l], a[m] = a[m], a[l]
#             l = l + 1
#             m = m + 1
#         elif a[m] == 1:
#             m = m + 1
#         else:
#             a[m], a[h] = a[h], a[m]
#             h = h - 1
#     return a
     

# # Driver Program
# arr = []
# n=int(input("Enter number of elements: "))
# print("Enter elements: ")
# for i in range(0,n):
#     arr.append(int(input()))

# print("Given array: ",arr)
# arr = sort012( arr, n)
# print ("Array after segregation :",arr)


