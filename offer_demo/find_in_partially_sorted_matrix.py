'''
@filename		:FindInPartiallySortedMatrix.py
@Description	:在一个行列分别有序的矩阵中, 寻找一个目标值的坐标
@Date			:2022/01/12 10:37:31
@Author      	:hjd
@version      	:1.0
'''


def find(data, value):
    result = []
    if data:
        rows, cols = len(data), len(data[0])
        row, col = 0, cols - 1
        while (row < rows) and col >= 0:
            if data[row][col] == value:
                result = [row, col]
                break
            elif data[row][col] > value:
                col -= 1
            else:
                row += 1
    return result


if __name__ == '__main__':
    data = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]

    print(find(data, 13))
