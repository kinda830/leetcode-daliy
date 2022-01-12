'''
@filename		:number_of_one.py
@Description	:求 一个数字的二进制 1 的个数
@Date			:2022/01/12 10:56:02
@Author      	:hjd
@version      	:1.0
'''


def number_of_one(n):
    count = 0

    while n:
        count += 1
        n = (n - 1) & n
    return count


if __name__ == '__main__':
    print(number_of_one(9))
