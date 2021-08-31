# 나중에 다시 풀어보쟈,,
import sys
input = sys.stdin.readline
while True:
    sentence = input().rstrip()
    stack=[]
    true_flag=1
    if sentence =='.':
        break
    for i in sentence:
        if i =='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                true_flag=0
                break
        elif i==']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag=0
                break
    if sentence == '.':
        break
    print('yes' if true_flag and not(stack) else 'no')


# import sys
# input = sys.stdin.readline
# while 1:
#     string = input().rstrip()
#     stack = []
#     true_flag = 1
#     for cha in string:
#         if cha == '(' or cha == '[':
#             stack.append(cha)
#         elif cha == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#         elif cha == ']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#     if string == '.':
#         break
#     print("yes" if true_flag and not(stack) else "no")











# braket_list=['(',')','[',']']
# zero_list =[0,0,0,0]
# while True:
#     d = {'(': 0, ')': 0, '[': 0, ']': 0}
#     result_list=[]
#     sentence = input()
#     if sentence == ".":
#         break
#     count_d = {'(':0,')':0,'[':0,']':0}
#     count =0
#     for i in sentence:
#         count+=1
#         if i in braket_list:
#             if count_d[i] == 0:
#                 count_d[i]=count
#             d[i]+=1
#             print(d, count_d)
#     if (d['('] == d[')'] and d['['] == d[']'] and count_d['('] < count_d[')'] and count_d['['] < count_d[']']) or (list(d.values()) == zero_list):
#         print('yes')
#     else:
#         print('no')
