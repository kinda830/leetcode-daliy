'''
@file        :number_of_one.py
@Description: 求 一个数字的二进制 1 的个数
@Date     :2021/12/25 15:59:47
@Author      :kinda
@version      :1.0
'''


def number_of_one(n):
    count = 0

    while n:
        count += 1
        n = (n - 1) & n
    return count


if __name__ == '__main__':
    print(number_of_one(9))
