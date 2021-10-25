n = int(input())
cnt=1
result=0
while True:
    result += 6*cnt
    if n !=1:
        if result >= n-1:
            print(cnt+1)
            break
    else:
        print(1)
        break
    cnt+=1