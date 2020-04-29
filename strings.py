MAX_CHAR = 256
# def frc(s):
#     p = -1
#     st = [0 for i in range(MAX_CHAR)]
#
#     pos = [0 for i in range(MAX_CHAR)]
#
#     for i in range(len(s)):
#         k = ord(s[i])
#         if st[k]==0:
#             st[k]+=1
#             pos[k]=i
#         elif st[k]==1:
#             st[k]+=1
#     for i in range(MAX_CHAR):
#         if st[i]==2:
#             if p==-1:
#                 p = pos[i]
#             elif(p>pos[i]):
#                 p = pos[i]
#     return p
# ab="pranshupareekp"
# ind=frc(ab)
# print(ab[ind])

def lexr(arr):
    count=[0 for i in range(MAX_CHAR)]
    for i in range(len(arr)):
        count[ord(arr[i])]+=1
    for i in range(MAX_CHAR):
        count[i]=count[i-1]+count[i]

