'''
@filename		:straight_sort.py
@Description	:直接插入排序
@Date			:2022/01/11 16:48:38
@Author      	:hjd
@version      	:1.0
'''


def straight_sort(numbers):

    for i in range(1, len(numbers)):
        tmp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > tmp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = tmp

    return numbers


if __name__ == "__main__":
    numbers = [1, 2, 7, 23, 54, 3, 5, 7, 21, 4]
    print(straight_sort(numbers))
