'''
@file        :IsPopOrder.py
@Description :
@Date        :2022/01/04 21:44:45
@Author      :kinda
@version     :1.0
'''


class Stack(object):
    def __init__(self) -> None:
        super().__init__()
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        number = self.stack.pop()
        return number

    def top(self):
        return self.stack[-1]

    def lenght(self):
        return len(self.stack)


def is_pop_order(p_push, p_pop):
    flag = False

    if p_pop and p_push and len(p_pop) == len(p_push):
        stack_data = Stack()
        pop_index = 0
        push_index = 0
        while pop_index < len(p_pop):
            while stack_data.lenght() == 0 or stack_data.top() != p_pop[pop_index]:
                if push_index == len(p_push):
                    break
                stack_data.push(p_push[push_index])
                push_index += 1

            if stack_data.top() != p_pop[pop_index]:
                break

            stack_data.pop()
            pop_index += 1

        if stack_data.lenght() == 0 and pop_index == len(p_pop):
            flag = True

    return flag


if __name__ == "__main__":
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 5, 2, 1]

    print(is_pop_order(push, pop))
