class Solution(object): 

    def swap(self,a,ind1,ind2):
        a[ind1],a[ind2]=a[ind2],a[ind1]
        return a

        
    def reverse(self,a,b,e):
        while b<e:
            self.swap(a,b,e)
            b+=1
            e-=1
            return a
        
        
    def nextPermutation(self,a):
        if len(a)==1:
            return
        if len(a)==2:
            return self.swap(a,0,1)
        
        dec=len(a)-2
        while dec>=0 and a[dec]>=a[dec+1]:
            dec-=1
            self.reverse(a,dec+1,len(a)-1)
        
        if dec==-1:
            return
        next_num = dec+1
        while next_num < len(a) and a[next_num]<=a[dec]:
            next_num+=1
            self.swap(a,next_num,dec)

def printarr(a,n):
    for i in range(n):
        print(a[i],end=' ')

a = []
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    a.append(int(input()))
print("Given array: ",a)

obj1=Solution()
obj1.nextPermutation(a)
printarr(a,n)

# class Solution(object):
#     def nextPermutation(self, nums):
#         found = False
#         i = len(nums)-2
#         while i >=0:
#             if nums[i] < nums[i+1]:
#                 found =True
#                 break
#             i-=1
#         if not found:
#             nums.sort()
#         else:
#             m = self.findMaxIndex(i+1,nums,nums[i])
#             nums[i],nums[m] = nums[m],nums[i]
#             nums[i+1:] = nums[i+1:][::-1]
#         return nums
#     def findMaxIndex(self,index,a,curr):
#         ans = -1
#         index = 0
#         for i in range(index,len(a)):
#             if a[i]>curr:
#                 if ans == -1:
#                     ans = curr
#                     index = i
#                 else:
#                     ans = min(ans,a[i])
#                     index = i
#         return index
    
# ob1 = Solution()
# print(ob1.nextPermutation([1,2,5,4,3]))


