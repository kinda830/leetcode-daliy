'''
@filename		:check_valid_string.py
@Description	:
    给定一个只包含三种字符的字符串：（，）和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

    1. 任何左括号 ( 必须有相应的右括号 )。
    2. 任何右括号 ) 必须有相应的左括号 (。
    3. 左括号 ( 必须在对应的右括号之前 )。
    4. * 可以被视为单个右括号 )，或单个左括号 (，或一个空字符串。
    5. 一个空字符串也被视为有效字符串。
@Date			:2022/01/13 14:42:44
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


def check_valid_string(s):
    result = True
    if s:
        all = Stack()
        left = Stack()

        for i, ss in enumerate(s):
            if ss == "(":
                left.push(i)
            elif ss == "*":
                all.push(i)
            else:
                if left.length():
                    left.pop()
                elif all.length():
                    all.pop()
                else:
                    result = False
                    break
        if left.length() != 0:
            if all.length() != 0 and left.length() <= all.length():
                for _ in range(left.length()):
                    l = left.pop()
                    a = all.pop()
                    if l > a:
                        result = False
            else:
                result = False
    return result


if __name__ == "__main__":
    s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

    print(check_valid_string(s))
