a=int(input())
lst=sorted(list(map(int, input().split())))
sum=0
for i in range(len(lst)):
    for j in lst[:i+1] :
        sum+=j

print(sum)