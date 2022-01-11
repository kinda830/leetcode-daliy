'''
@filename		:mao_pao_sort.py
@Description	:冒泡排序
@Date			:2022/01/11 16:38:06
@Author      	:hjd
@version      	:1.0
'''


def mao_pao_sort(numbers):

    if numbers:
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


if __name__ == "__main__":
    numbers = [1, 2, 7, 23, 54, 3, 5, 7, 21, 4]
    print(mao_pao_sort(numbers))
