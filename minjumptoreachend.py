# T(n)= O(n^2)   s(n) = O(1)

# greedy method:
# def minJumps(a):
#         jumps = 0
#         current_jump_end = 0
#         farthest = 0
#         for i in range(len(a) - 1):
#             farthest = max(farthest, i + a[i])
#             if i == current_jump_end:
#                 jumps += 1
#                 current_jump_end = farthest
#         return jumps


# dynamic programming: O(n^2) s= O(n)
def minJumps(a, n):
    dp = [n] * (99999999)
    dp[0] = 0
    for i in range(n):
        for j in range(i+1,  min(i+a[i]+1, n)):
            dp[j] = min(dp[j], 1 + dp[i])
    return dp[n-1]

# # Bruteforce
# def minjumps(a,n,pos):
#     if pos >= n-1:
#         return -1
#     minjump = 9999999999999
#     maxsteps = a[pos]
#     while maxsteps > 0:
#         minjump = min(minjump,1+minjumps(a,n,pos+maxsteps))
#         maxsteps-=1
#     return minjump

a = []
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(0,n):
    a.append(int(input()))
print("Given array: ",a)

print("Minimum number of jumps to reach is ",minJumps(a,n))
