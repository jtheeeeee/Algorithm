n, k = map(int, input().split())
coin_list = []
num = 0
for _ in range(n):
    coin_list.append(int(input()))
for i in range(len(coin_list)-1, -1, -1):
    if k == 0:
        break
    if coin_list[i] > k:
        continue
    num += k // coin_list[i]
    k %= coin_list[i]

print(num)