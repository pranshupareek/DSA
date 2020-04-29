# # Rotation of array
# # my solution but require more splace
# arr=[1,2,3,4,5]
# rt=2
# temp=[]
# for i in range(len(arr)):
#     temp.append(arr[(i+rt)%len(arr)])
# arr=temp[:]
# print(arr)

# Storing rain water

# arr=[3,0,10,5,7]
#
# def findWater(arr, n=len(arr)):
#     # left[i] contains height of tallest bar to the
#     # left of i'th bar including itself
#     left = [0] * n
#
#     # Right [i] contains height of tallest bar to
#     # the right of ith bar including itself
#     right = [0] * n
#
#     # Initialize result
#     water = 0
#
#     # Fill left array
#     left[0] = arr[0]
#     for i in range(1, n):
#         left[i] = max(left[i - 1], arr[i])
#
#         # Fill right array
#     right[n - 1] = arr[n - 1]
#     for i in range(n - 2, -1, -1):
#         right[i] = max(right[i + 1], arr[i]);
#
#         # Calculate the accumulated water element by element
#     # consider the amount of water on i'th bar, the
#     # amount of water accumulated on this particular
#     # bar will be equal to min(left[i], right[i]) - arr[i] .
#     for i in range(0, n):
#         water += min(left[i], right[i]) - arr[i]
#
#     return water
#
# print(findWater(arr)


# # Python3 program to find out maximum
# # profit by buying and/ selling a share
# # at most k times given the stock price
# # of n days
#
# # Function to find out maximum profit
# # by buying & selling/ a share atmost
# # k times given stock price of n days
# def maxProfit(price, n, k):
#     # Table to store results of subproblems
#     # profit[t][i] stores maximum profit
#     # using atmost t transactions up to
#     # day i (including day i)
#     profit = [[0 for i in range(n + 1)]
#               for j in range(k + 1)]
#
#     # Fill the table in bottom-up fashion
#     for i in range(1, k + 1):
#         prevDiff = float('-inf')
#
#         for j in range(1, n):
#             prevDiff = max(prevDiff,
#                            profit[i - 1][j - 1] -
#                            price[j - 1])
#             profit[i][j] = max(profit[i][j - 1],
#                                price[j] + prevDiff)
#
#     return profit[k][n - 1]



# # Prefix susm array
# # example 1 if we need to calculate the sum of element from index l to r
#
# arr=[12,5,9,4,5,3,9,42,25,3,2,5,15,2,4,524,2,4,554,2,5]
#
# ps=[]
# summ=0
# for i in range(len(arr)):
#     summ+=arr[i]
#     ps.append(summ)
#
# def ans(l,r,ps=ps):
#     if l==0:
#         return ps[r]
#     else:
#         return ps[r]-ps[l-1]
#
# print(ans(0,5))

# # example 2 Given n ranges find the maximum appearing element in the ranges.
#
# L = [2, 4, 5, 13]
# R = [6, 7, 12, 20]
#
# # L = [1, 2, 3]
# # R = [3, 5, 7]
#
# maxlen = 100
#
# jda = [0] * maxlen
#
# for i in L:
#     jda[i] = 1
# for i in R:
#     jda[i + 1] = -1
#
# # calculating prefix sum now
# psa = []
# summ = 0
# maxn = 0
# maxxi = 0
# for i in range(maxlen):
#     summ += jda[i]
#     psa.append(summ)
#     if maxn<summ:
#         maxn=summ
#         maxxi=i
#
# print(maxxi)




# # is it possible to divide an array in three equal parts
# arr = [5, 2, 6, 1, 1, 1, 5]
# ts = 0
# for i in range(len(arr)):
#     ts += arr[i]
# presum = 0
# st = 1
# anss = 0
# for i in range(len(arr)):
#     ts -= arr[i]
#     presum += arr[i]
#     if 2 * presum == ts and st == 1:
#         presum = 0
#         st = 2
#
#     elif st == 2 and presum == ts:
#         print("Possible")
#         anss = 1
#         break
# if anss != 1:
#     print("Not possible")


