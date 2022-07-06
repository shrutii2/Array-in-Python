''' Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6 
Explanation:
The set goes like 3,4,7,9,9 and the output 
is 9-3 = 6'''

# t(n)=O(nlogn) for sorting s(n)=O(1)

def findmindiff(a,n,m):
    if(m==0 or n==0):
        return 0

    if(n<m):
        return -1

    a.sort()
    mindiff=a[n-1]-a[0]

    for i in range(n-m+1):
        mindiff=min(mindiff,a[i+m-1]-a[i])
    return mindiff

a=[3, 4, 1, 9, 56, 7, 9, 12]
m=5         #number of students and number of packets which need
n=8
print("The minimum difference between maximum chocolates and minimum chocolates is",findmindiff(a,n,m),"\n by choosing following %d packets."%m)