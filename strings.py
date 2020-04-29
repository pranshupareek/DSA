import math

MAX_CHAR = 256

# First occurrence of Repeated or Non repeated string
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
# ab="pranshupareek"
# ind=frc(ab)
# print(ab[ind])

#Find Lexicographic Rank

def lexr(arr):
    count=[0 for i in range(MAX_CHAR)]
    for i in range(len(arr)):
        count[ord(arr[i])]+=1
    for i in range(MAX_CHAR):
        count[i]=count[i-1]+count[i]
    lenn=0
    j=0
    for i in range(MAX_CHAR):
        if count[i]!=0:
            lenn=lenn+j*math.factorial(count[i])
            j+=1
    return lenn
a="string"
lexr(a)

