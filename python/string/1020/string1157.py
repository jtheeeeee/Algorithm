
i = input().upper()

def string_array(string):
    alpha_list = [0]*26
    for char in i:
        char_index=ord(char)-ord("A")
        alpha_list[char_index]+=1

    return alpha_list

alpha_list=string_array(i)
max_num=max(alpha_list)

if alpha_list.count(max_num) ==1:
    print(chr(alpha_list.index(max_num)+65))
else:
    print('?')