
# num = input()
# 정렬을 위해 아래와 같이 리스트를 선언해서 만들 필요가 없다. 문자열도 sorted()를 사용하면 정렬이 가능하다. 하지만 새로운 변수를 선언해 주어야 한다.
# arr=[]
# for i in num:
#     arr.append(int(i))
# for i in sorted(arr,reverse=True):
#     print(i,end='')
#
# 정렬된 문자열을 for문 사용 없이 합치는 방법으로 join() 함수를 사용한다.
# 문자열 반환
print(''.join(reversed(sorted(input()))))
