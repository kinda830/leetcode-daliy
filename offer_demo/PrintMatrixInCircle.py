'''
@file        :PrintMatrixInCircle.py
@Description: 顺时针打印一个矩阵
@Date     :2021/12/30 21:25:40
@Author      :kinda
@version      :1.0
'''


def print_matrix_in_circle(numbers, start):
    end_x = len(numbers[0]) - 1 - start
    end_y = len(numbers) - 1 - start

    # 从左到右打印一行
    for i in range(start, end_x + 1):
        number = numbers[start][i]
        print(number)

    # 从上到下打印一列
    if start < end_y:
        for i in range(start + 1, end_y + 1):
            print(numbers[i][end_x])

    # 从右到左打印一行
    if start < end_x and start < end_y:
        a = [i for i in range(start, end_x)]
        for i in a[::-1]:
            print(numbers[end_y][i])

    # 从下到上打印一列
    if start < end_x - 1 and start < end_y - 1:
        a = [i for i in range(start + 1, end_y)]
        for i in a[::-1]:
            print(numbers[i][start])


def print_matrix_clock_wisely(numbers):
    if numbers:
        start = 0
        while len(numbers[0]) > start * 2 and len(numbers) > start * 2:
            print_matrix_in_circle(numbers, start)
            start += 1


if __name__ == "__main__":
    numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

    print_matrix_clock_wisely(numbers)
