a = int(input())

def recursion(num):
    if num > 1:
        return num *recursion(num-1)
    else:
        return 1
print(recursion(a))