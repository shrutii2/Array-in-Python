# # Given an array of size n, find all elements in array that appear more than n/k times. 
# # For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3].
# # Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times.
# # There are two elements that appear more than two times, 2 and 3.

# T(n)=O(n^2)

def appears(a,n,k):
    new={}                     #for initializing map
    for i in range(n):
        if a[i] in new:
            new[a[i]]+=1
        else:
            new[a[i]]=1
    
    for i in new:
        if(new[i]>n/k):
            print(i)

a=[3,1,2,2,1,2,3,3]
k=4
n=len(a)
appears(a,n,k)
