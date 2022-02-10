'''
@file        :generateParenthesis.py
@Description :数字 n 代表生成括号的对数, 请你设计一个函数, 用于能够生成所有可能的并且 有效的 括号组合。1=<n=<8
@Date        :2022/01/11 22:32:59
@Author      :kinda
@version     :1.0
'''


def generate_parent_thesis(n):
    ans = []

    def bracktrack(s, left, right):
        if len(s) == 2 * n:
            ans.append("".join(s))
            return

        if left < n:
            s.append("(")
            bracktrack(s, left + 1, right)
            s.pop()
        if left > right:
            s.append(")")
            bracktrack(s, left, right + 1)
            s.pop()

    bracktrack([], 0, 0)
    return ans


if __name__ == "__main__":
    print(generate_parent_thesis(3))
