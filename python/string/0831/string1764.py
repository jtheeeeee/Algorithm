import sys
# a,b = map(int,sys.stdin.readline().split())
# name =[]
# str=''
# num =0
# for i in range(a):
#     name.append(sys.stdin.readline())
# for i in range(b):
#     temp_name=sys.stdin.readline()
#     if temp_name in name:
#         num+=1
#         str+=(temp_name+'\n')
#
# print(num)
# print(str)

# set을 사용한다는 생각을 하지 못했다

# a,b = map(int,sys.stdin.readline().split())
# nolisten=set()
# nolook = set()
# for _ in range(a): nolisten.add(sys.stdin.readline().rstrip())
# for _ in range(b): nolook.add(sys.stdin.readline().rstrip())
# print(len(sorted(nolisten&nolook)))
# print('\n'.join(sorted(nolisten&nolook)))

a,b = map(int,sys.stdin.readline().split())
name_list=sys.stdin.read().splitlines()
nolisten = set(name_list[:a])
nolook = set(name_list[a:])
res=list(nolisten & nolook)
print(len(res))
for i in res:
    print(i)


