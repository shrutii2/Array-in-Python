
def arrayManipulation(n, queries):
    l=[0]*(n+1)
    for a,b,k in queries:
        l[a]+=k
        if b+1<=n:
            l[b+1]-=k
    maxx=summ=0
    for i in l:
        summ+=i
        if summ>maxx:
            maxx=summ
    return maxx

n=5
queries=[[1,2,100],[2,5,100],[3,4,100]]
res=arrayManipulation(n,queries)
print(res)