# T(n) = O(n)     S(n) = O(1)

def duplicate(a):
    

    ''' for printing only 1 duplicates value
    x=y=a[0]
    while True:
        x=a[x]
        y=a[a[y]]
        if x==y:
            break
    x=a[0]
    while x!=y:
        x=a[x]
        y=a[y]
    print("repeating values are:",y)'''

    # this is not right bcoz its only get answer proper when input value is less than n
    # for i in range(n):
    #     x=a[i]%n
    #     a[x]+=n
    # print("Repeating values are:")
    # for i in range(n):
    #     if(a[i]>=n*2):
    #         print(i,' ')
    


a = []
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    a.append(int(input()))
print("Given array: ",a)
duplicate(a)