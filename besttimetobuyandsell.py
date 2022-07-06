#T(n) = O(n)       S(n) = O(1)

import sys

def maxtwobuysell(arr, size):
	first_buy = -sys.maxsize
	first_sell = 0
	second_buy = -sys.maxsize
	second_sell = 0

	for i in range(size):

		first_buy = max(first_buy, -arr[i])
		first_sell = max(first_sell, first_buy + arr[i])
		second_buy = max(second_buy, first_sell - arr[i])
		second_sell = max(second_sell, second_buy + arr[i])

	
	return first_sell,second_sell

if __name__ == '__main__':
	arr = [ 7,1,5,3,6,4 ]
	size = len(arr)
	print(maxtwobuysell(arr, size))




# def maxprofit(prices,n):
#     l,r=0,1
#     maxp=0

#     while r < len(prices):
#         if prices[l] < prices[r]:
#             profit = prices[r] - prices[l]
#             maxp = max(maxp,profit)
#         else:
#             l+=1
#             r+=1
#     return maxp

# prices=[7,1,5,3,6,4]
# print("Maximum profit is : ",maxprofit(prices))


# def findMaximumProfit(prices, i,  k,buy, v):

#     # If no stock can be chosen
#     if (i >= len(prices) or k <= 0):
#         return 0

#     if (v[i][buy] != -1):
#         return v[i][buy]

#     # If a stock is already bought
#     if (buy):
#         v[i][buy] = max(-prices[i]+ findMaximumProfit(prices, i + 1,k, not buy, v),findMaximumProfit(prices, i + 1, k,buy, v))
#         return v[i][buy]

#     else:
#         # Buy now
#         v[i][buy] = max(prices[i]+ findMaximumProfit(prices, i + 1, k - 1, not buy, v),findMaximumProfit(prices, i + 1, k,buy, v))
#         return v[i][buy]

# def maxProfit(prices):
#     n = len(prices)
#     v = [[-1 for x in range(2)]for y in range(n)]

#     # buy = 1 because atmost one transaction is allowed
#     return findMaximumProfit(prices, 0, 1, 1, v)

# prices=[7,1,5,3,6,4]
# ans=maxProfit(prices)
# print(ans)