# T(n) = O(n)    S(n) = O(1)

import array as A
a = A.array('i',[1 ,2, 3, 4])
for i in range(0,len(a)):
    print(a[i])

#option1: swapping

# def reverse (a,start,end):
#     if start>=end:        # or while start<end
#         return
#     a[start],a[end]=a[end],a[start]
#     # reverse(a,start+1,end-1)  OR       # start+=1 # end-=1
    

# reverse(a,0,3)
# print(a)


# option2: slicing

def reverse(a):
    return a[::-1]     #right one acc to hackerrank

print("REverse array is")
print(reverse(a))



