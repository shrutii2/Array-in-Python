# t(n) = O(nlogn) for sorting arr    and S(n)=O(1)


def findLongestConsecutiveSubsequence(a):
    ans=0
    count=0
    a.sort()
    p=[]
    p.append(a[0])
    for i in range(1,len(a)):            #for no duplicate elements
        if (a[i]!= a[i-1]):
            p.append(a[i])
    for i in range(len(p)):              #find max length by traversing an array 
        if (i>0 and p[i]==p[i-1]+1):
            count+=1
        else:
            count=1
        ans=max(ans,count)
    return ans
    


a=[1,2,2,3]
n=4
print("Longest contiguous subsequence length is ",findLongestConsecutiveSubsequence(a))