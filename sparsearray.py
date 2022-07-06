from collections import Counter

def matchingStrings(strings, queries):
    # create a dict with count
    s=Counter(strings)
    res=[]
    # processing queries
    for q in queries:
        res.append(s[q])
        
    return res


strings=['aba','baba','aba','xzzb']
queries=['aba','xzzb','ab']
res=matchingStrings(strings,queries)
print(res)