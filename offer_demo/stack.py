'''
@filename		:stack.py
@Description	:栈的定义类
@Date			:2022/01/13 15:31:57
@Author      	:hjd
@version      	:1.0
'''


class Stack(object):
    def __init__(self) -> None:
        super().__init__()
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)

    def length(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]
