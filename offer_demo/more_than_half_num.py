'''
@filename		:MoreThanHalfNum.py
@Description	:数组中出现次数超过—半的数字
@Date			:2022/01/10 17:26:19
@Author      	:hjd
@version      	:1.0
'''


def more_half_num(numbers):
    number, count = numbers[0], 1

    for n in numbers[1:]:
        if count == 0:
            number = n
            count = 1
        if n != number:
            count -= 1
        else:
            count += 1

    return number


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 4, 4, 4, 4, 5, 4, 6, 4]

    print(more_half_num(numbers))
