
# def new_num(a):
#     f_num = a // 10
#     s_num = a % 10
#     result = s_num*10+(f_num+s_num)%10
#     return result
#
# def ten_under(a):
#     result = a* 10+a
#     return result
#

a=int(input())
temp=a
i=1
while True:
    f_num=temp//10
    s_num =temp%10
    result = s_num * 10 + (f_num + s_num) % 10
    if result ==a:
        print(i)
        break
    i+=1
    temp=result


