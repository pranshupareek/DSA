#**Most important for strings is KMP ALGO**
#Permutaion of pattern exist
def ifAnagramPresent(txt,pat):
    counttxtw=[0]*256
    countpat=[0]*256
    for i in range(len(pat)):
        counttxtw[ord(txt[i])]+=1
        countpat[ord(pat[i])]+=1

    for i in range(len(pat),len(txt)):
        if countpat==counttxtw:
            return True
        counttxtw[ord(txt[i])]+=1
        counttxtw[ord(txt[i-len(pat)])]-=1
    return False
# str1='pranshu'
# pat1='sanhp'
# anss=ifAnagramPresent(str1,pat1)
# print(anss)


# import math
#
# MAX_CHAR = 256
#
#
# # First occurrence of Repeated or Non repeated string
# # def frc(s):
# #     p = -1
# #     st = [0 for i in range(MAX_CHAR)]
# #
# #     pos = [0 for i in range(MAX_CHAR)]
# #
# #     for i in range(len(s)):
# #         k = ord(s[i])
# #         if st[k]==0:
# #             st[k]+=1
# #             pos[k]=i
# #         elif st[k]==1:
# #             st[k]+=1
# #     for i in range(MAX_CHAR):
# #         if st[i]==2:
# #             if p==-1:
# #                 p = pos[i]
# #             elif(p>pos[i]):
# #                 p = pos[i]
# #     return p
# # ab="pranshupareek"
# # ind=frc(ab)
# # print(ab[ind])
#
# # Find Lexicographic Rank
#
# def lexr(arr):
#     count = [0 for i in range(MAX_CHAR)]
#     for i in range(len(arr)):
#         count[ord(arr[i])] += 1
#     for i in range(MAX_CHAR):
#         count[i] = count[i - 1] + count[i]
#     print("InsideLex",arr)
#
#
# def fact(n):
#     return 1 if n <= 1 else n * fact(n - 1)
#
# def upd(c):
#     for i in range(ord(c),MAX_CHAR):
#         count[i]-=1
#     print("InsideUPD",c)
#
# def findr(arr):
#     lenn=len(arr)
#     mul = fact(lenn)
#     rank = 1
#     lexr(arr)
#
#     for i in range(lenn):
#         print("Loop")
#         mul = mull//(lenn-i)
#         rank+=count[ord(arr[i])-1]*mul
#         upd(arr[i])
#     return rank
#
# a = "string"
# an = lexr(a)
# print(an)

def rotck(str1,str2):
    strm=str1+str1
    if len(str2)==len(str1):
        for i in range(len(strm)):
            ts=strm[i:i+len(str2)]
            if ts==str2:
                return True
    return False

# str1="abcd"
# str2="bcda"
# print(rotck(str1,str2))
