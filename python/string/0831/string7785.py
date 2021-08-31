# n = int(input())
# in_list=[]
# for i in range(n):
#     log = input()
#     if "enter" in log:
#         in_list.append(log.replace(" enter",""))
#     elif "leave" in log:
#         if log.replace(" leave",'') is not None :
#             in_list.remove(log.replace(" leave",''))
#
# for i in reversed(sorted(in_list)):
#     print(i)

import sys
read = sys.stdin.readline

d = {}
for _ in range(int(read())):
    # 문자열을 비교하는 것보다 딕셔너리 형태로 쪼개서 구분하는 것이 낫다.
    name, action = read().split()
    if action == 'enter':
        d[name] = True
    elif action == 'leave':
        if name in d:
            del d[name]
# for문으로 문자열을 출력하지 않아도 된다,,
print('\n'.join(sorted(d.keys(), reverse=True)))