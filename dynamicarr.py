# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries

'''INCOMPLETE'''

def dynamicArray(n, queries):
    # intializing variable
    arr=[[] for _ in range(n)]
    lastans=0
    result=[]
    
    # mainlogic
    for query,x,y in queries:
        if query==1:
            index=(x^lastans)%n
            arr[index].append(y)
        else:
            index=(x^lastans)%n
            value=y%len(arr[index])
            lastans=arr[index][value]
            result.append(lastans)
            
    return result


n=int(input("n="))
queries=int(input("query="))
querie=[]
for i in range(queries):
    querie.append(i)
# queries=[1,0,5]
# queries=[1,1,7]
# queries=[1,0,3]
# queries=[2,1,0]
# queries=[2,1,1]
result = dynamicArray(n, queries)
print(result)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     q = int(first_multiple_input[1])

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

    # result = dynamicArray(n, queries)
    

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
# 2 5
# 1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1
# op:
# 7
# 3