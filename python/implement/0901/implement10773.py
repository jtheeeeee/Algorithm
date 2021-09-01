import sys
input=sys.stdin.readline
n = int(input())
lst=[]
for _ in range(n):
    a=int(input())
    if a==0:
        # pop의 쓰임을 잘 이해하지 못해서 헤맸음.
        lst.pop()
    else:
        lst.append(a)
print(sum(lst))
