# 한 층당 W개의 방
# H층
# ==> H * W 호텔

T= int(input())


for i in range(T):
    h,w,n=map(int, input().split())
    front = 0
    back = 0
    if n%h ==0:
        front = h*100
        back = n//h
    else:
        front = (n%h)*100
        back = 1 + n//h
    print(front+back)