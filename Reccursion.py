def sod(n):
    if n < 10:
        return n
    return sod(n // 10) + n % 10


#
# n = int(input())
# summ=sod(n)
# print(summ)

def maxcut(n, a, b, c):
    if n < 0:
        return -1
    if n == 0:
        return n
    res = max(maxcut(n - a, a, b, c), maxcut(n - b, a, b, c), maxcut(n - c, a, b, c))
    if res==-1:
        return -1
    return res + 1

def subseq(strn , curr="" , index=0):
    if index==len(strn):
        print(curr,end=" ")
        return
    subseq(strn,curr,index+1)
    subseq(strn,curr+strn[index],index+1)

subseq("ABC")
































# print(maxcut(9,2,2,2))

# i=7
# while i>0:
#     i-=3
#     print('*')
#     if i<=2:
#         break
# else:
#         print('*')

# val=154
# while(not(val)):
#     val**=2
# else:
#     val//=2
#
# print(val)
#
# n,m=[int(n) for n in input().split()]
# p=[]
# b=[]
# for i in range(n):
#     x,y=[int(x) for x in input().split()]
#     if y in b:
#         if(p[b.index(y)]<x):
#             p[b.index(y)]=x
#     else:
#         p.append(x)
#         b.append(y)
# print(sum(p))

# test = int(input())
# while (test):
#     test -= 1
#     n = int(input())
#     ans = 0
#     s = []
#
#     val = list(map(int, input().split()))
#     for i in range(n):
#         if (s == []):
#             s.append(val[i])
#         else:
#             ans = max(ans, val[i] | s[-1])
#             while (s != [] and s[-1] > val[i]):
#                 s.pop()
#                 if (s != []):
#                     ans = max(ans, val[i] | s[-1])
#             s.append(val[i])
#     print(ans)

# t=int(input())
# while t:
#     t-=1
#     n=int(input())
#     l=[]
#     ans=0
#     v=list(map(int,input().split()))
#     for i in range(0,n):
#         if l==[]:
#             l.append(v[i])
#         else:
#             ans=max