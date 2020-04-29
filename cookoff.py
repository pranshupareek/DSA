# def cntf(a,b):
#     if a>b:
#         return a-b
#     else:
#         return b-a
#
# t=int(input())
# while t:
#     t-=1
#     n,q=input().split()
#     n=int(n)
#     q=int(q)
#     ts=0
#     ic=0
#     for i in range(q):
#         f,d=input().split()
#         f=int(f)
#         d=int(d)
#         ts+=cntf(ic,f)+cntf(f,d)
#         ic=d
#     print(ts)



t=int(input())
while t:
    t-=1
    n,q=input().split()
    n = int(n)
    q=int(q)
    anss=0
    for i in range(1,2*n-1,2):
        q = q ** (i + 1) % 1000000007
        print(q)
        anss=(anss%1000000007+q%1000000007)%1000000007
    print(anss,q)
