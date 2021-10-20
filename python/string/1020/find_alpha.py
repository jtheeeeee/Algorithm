
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a") #a의 ascii : 97
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alpha_list = find_alphabet_occurrence_array(string)
    max_index= alpha_list.index(max(alpha_list))+ord("a")
    return chr(max_index)


result = find_max_occurred_alphabet(input)
print(result)