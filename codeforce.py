# import math
# t=int(input())
# while t:
#     t-=1
#     n=int(input())
#     po2=4
#     i=1
#     while 1:
#         if n%(po2-1)==0:
#             print(n//(po2-1))
#             break
#         else:
#             po2*=2
#         i+=1
#



# t=int(input())
# while t:
#     t-=1
#     n=int(input())
#     if n%4==0:
#         print("YES")
#         for i in range(1,n//2+1):
#             print(2*i,end=" ")
#         for i in range(1,n//2):
#             print(2*i-1,end=" ")
#         print(n-1+n//2)
#     else:
#         print("NO")


t=int(input())
while t:
    t-=1
    n=int(input())
    a=[int(j) for j in input().split()]
    minn=0
    maxx=0
    summ=0
    for i in range(n):
        if a[i] > 0:
            npc = 0
            minn=0
        else:
            npc = 1
            maxx=0
        if npc%2==0:
            if maxx<a[i]:
                summ-=maxx
                maxx=a[i]
                summ+=maxx
            else:
                continue
        else:
            if minn<a[i] or minn==0:
                summ-=minn
                minn=a[i]
                summ+=minn
            else:
                continue
    print(summ)