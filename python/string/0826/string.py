# backjoon 2941
# s= input()
# char_list =['c-','c=','d-','dz','lj','nj','s=','z=']
# count = 0
# i=0
# except_list=['-','=','q','w','x']
# while i <len(s):
#     if s[i:i+2] in char_list:
#         count+=1
#         i+=1
#         if s[i-1:i+1]=='dz' and s[i+1:i+2] != '=' :
#             count -=1
#     else:
#         if s[i:i+1] in except_list:
#             i+=1
#             continue
#         count+=1
#     i+=1
# print(count)
#특정 문자열을 list로 만들어야 겠다는 접근법 까지는 꽤 좋았으나
#특정 문자열을 하나의 단어로 대체하겠다는 접근은 하지 못함..
s=input()
char_list =['c-','c=','d-','dz=','lj','nj','s=','z=']
for i in char_list:
    s = s.replace(i, "*")

print(len(s))