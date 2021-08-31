# word=list(input())
# arr=[]
# while len(word)>0:
#     arr.append(''.join(word))
#     word.pop(0)
# print('\n'.join(sorted(arr)))


word=input()
arr=[]
for i in range(len(word)):
    #pop 대신에 슬라이싱도 가능하다.
    arr.append(word[i:])
print('\n'.join(sorted(arr)))