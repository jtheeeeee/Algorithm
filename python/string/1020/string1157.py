import numpy
i = input().lower()


def string_array(string):
    alpha_list = [0]*26
    for char in i:
        char_index=ord(char)-ord("a")
        alpha_list[char_index]+=1

    return alpha_list


def find_max_alpha( alpha_list, max_num):
    if alpha_list.index(max(alpha_list)) == max_num:
        return(alpha_list.index(max(alpha_list)))
    else:
        return "?"


alpha_list=string_array(i)
print(alpha_list.index(max(alpha_list)))
print(find_max_alpha(alpha_list,max(alpha_list)))