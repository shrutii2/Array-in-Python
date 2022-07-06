
def miniMaxSum(arr):
    arr.sort()
    h = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        temp = 0
        for j in range(i,i+4):
            temp = temp + arr[j]
        h[i] = temp
    
    print(h[0],h[-1])

if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))

    arr=[1,2,3,4,5]
    miniMaxSum(arr)
