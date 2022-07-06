def factorial(n):
    if (n==1):
        return 1
    else:
        fact=(n)*factorial(n-1)
        return fact

a=factorial(5)
print(a)

# n=5
# num=n
# f=1
# while(n>0):
#     f=f*n
#     n-=1
# print(f"{num}! is {f}")
