# #Program for checking any subarray having the sum 0
# def cns(arr,n):
#     psa=[]
#     sm=0
#     for i in range(n):
#         sm+=arr[i]
#         psa.append(sm)
#     Hash=dict()
#     for i in range(n):
#         if psa[i]==0:
#             return i
#         elif psa[i] in Hash.keys():
#             return i
#         else:
#             Hash[psa[i]]=1
#     return -1
#
# a=[1,-1,3,4,5,6,7,-3,-4,9,10]
# anss=cns(a,len(a))
# if anss==-1:
#     print("False")
# else:
#     print("True")



# #Having given sum
#
# def cns(arr,n, gs):
#     psa=[]
#     sm=0
#     for i in range(n):
#         sm+=arr[i]
#         psa.append(sm)
#     Hash=dict()
#     for i in range(n):
#         if psa[i]==gs:
#             return i
#         elif psa[i]-gs in Hash.keys():
#             return i
#         else:
#             Hash[psa[i]]=1
#     return -1
#
# a=[1,-1,3,4,5,6,7,-3,-4,9,10]
# gs=int(input())
# anss=cns(a,len(a),gs)
# if anss==-1:
#     print("False")
# else:
#     print("True")

xyz=square(8)
print(xyz)