'''
@filename		:pennutation_for_str.py
@Description	:字符串的排列
@Date			:2022/01/10 11:37:26
@Author      	:hjd
@version      	:1.0
'''

def pennutation(s):
    if s:
        pennutation_core(list(s), 0)


def pennutation_core(s, i):
    if i >= len(s):
        print("".join(s))
    else:
        for begin in range(i, len(s)):
            s[begin], s[i] = s[i], s[begin]

            pennutation_core(s, i+1)

            s[begin], s[i] = s[i], s[begin]


if __name__ == "__main__":
    s = "abc"

    pennutation(s)