import sys
input=sys.stdin.readline


class Stack:
    def __init__(self):
        self.list=[]
        self.len=0

    def push(self, x):
        self.list.append(x)
        self.len+=1

    def pop(self):
        if self.size==0:
            return -1
        result= self.list[self.len-1]
        self.len-=1
        return result

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len==0 else 0

    def top(self):
        return self.list[-1] if self.size() != 0 else -1

