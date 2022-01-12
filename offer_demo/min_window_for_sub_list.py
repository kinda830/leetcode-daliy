'''
@file        :minWindowForSubList.py
@Description :长度最小的子数组且子数组的和等于目标值
@Date        :2022/01/09 14:53:51
@Author      :kinda
@version     :1.0
'''


def min_window(l, target):
    start, end = 0, 0
    tmp = l[0]
    min_length = len(l) + 1
    begin = 0
    result = []
    while end < len(l) and start < len(l) - 1:
        # tmp += l[end]

        if tmp == target and min_length > end - start + 1:
            min_length = end - start + 1
            begin = start
            tmp -= l[start]
            start += 1
        elif tmp > target:
            tmp -= l[start]
            start += 1
        elif tmp < target:
            end += 1
            tmp += l[end]

    if min_length < len(l) + 1:
        result = l[begin:begin + min_length]

    return result


if __name__ == "__main__":
    s = [2, 3, 1, 2, 4, 3]
    t = 7
    print(min_window(s, t))
