# T(n) = O(n^2)       and  S(n) = O(n)

#taking the inputs
a=[]
n=int(input("Enter the number of elements:"))
print("Enter the array elements")

for i in range(0,n):
   a.append(int(input()))

k=int(input("Enter the value of k:"))
l=int(input("Enter 1 for kth largest or 0 for kth smallest:"))

#sorting the list
a.sort()
# for i in range(0,n):
#    for j in range(0,n-i-1):
#          if(a[j]>a[j+1]):
#             t=a[j]
#             a[j]=a[j+1]
#             a[j+1]=t

#displaying the sorted array
print("\nThe sorted elements:",end=" ")

for i in range(0,n):
   print(a[i],end=" ")

#finding the kth largest element  O(n)
if l==1:
   for i in range(n-1,n-k-1,-1):
      m=0
   print("\nThe",k,"th largest element is:",a[i])

#finding the kth smallest element O(n)
else:
   for i in range(0,k):
      m=0
   print("\nThe",k,"th smallest element is:",a[i])




