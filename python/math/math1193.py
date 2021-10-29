def sum_r(i):
    sum_n = 0
    for i in range(1,i+1):
        sum_n += i
    return sum_n

x = int(input())
cnt=1
while True:
    if sum_r(cnt) >= x:
        idx = x - sum_r(cnt - 1)
        if cnt % 2 == 0:
            print(f'{idx}/{cnt+1-idx}')
        else:
            print(f'{cnt+1-idx}/{idx}')
        break
    cnt+=1

