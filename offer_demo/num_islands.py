'''
@filename		:num_islands.py
@Description	:
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
@Date			:2022/01/12 14:37:05
@Author      	:hjd
@version      	:1.0
'''


def dfs(numbers, x, y):
    nr, nc = len(numbers), len(numbers[0])

    numbers[x][y] = 0

    for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= i < nr and 0 <= j < nc and numbers[i][j] == 1:
            dfs(numbers, i, j)


def num_islands(numbers):
    islands_number = 0
    nr = len(numbers)
    if nr == 0:
        return islands_number
    nc = len(numbers[0])

    for i in range(nr):
        for j in range(nc):
            if numbers[i][j] == 1:
                islands_number += 1
                dfs(numbers, i, j)

    return islands_number


if __name__ == "__main__":
    numbers = [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0]
    ]
    print(num_islands(numbers))
