'''
@filename		:min_remove_to_make_valid.py
@Description	:
@Date			:2022/01/13 15:17:39
@Author      	:hjd
@version      	:1.0
'''
from stack import Stack


def min_remove_to_make_valid(s):
    result = []
    left = Stack()
    remove_list = []

    if s:
        for i, c in enumerate(s):
            if c == '(':
                left.push(i)
            elif c == ')':
                if left.length():
                    left.pop()
                else:
                    remove_list.append(i)
        for _ in range(left.length()):
            remove_list.append(left.pop())

        for i, c in enumerate(s):
            if i not in remove_list:
                result.append(c)
    return "".join(result)


if __name__ == "__main__":
    s = "(s(sd(kd)dss)"
    print(min_remove_to_make_valid(s))
