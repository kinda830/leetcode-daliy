'''
@Description:       :机器人的运动范围
@Date     :2021/12/23 22:49:14
@Author      :kinda
@version      :1.0
'''


def MovingCount(threshold, rows, cols):
    count = 0
    if threshold > 0:
        visited = [[False] * rows for _ in range(cols)]
        count = moving_count_core(threshold, rows, cols, 0, 0, visited)

    return count


def moving_count_core(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        visited[row][col] = True
        count = 1 + moving_count_core(
            threshold, rows, cols, row - 1, col, visited) + moving_count_core(
                threshold, rows, cols, row, col - 1, visited) + moving_count_core(
                    threshold, rows, cols, row + 1, col, visited) + moving_count_core(
                        threshold, rows, cols, row, col + 1, visited)
    return count


def check(threshold, rows, cols, row, col, visited):
    if row >= 0 and row < rows and col >= 0 and col < cols and getDigitSum(
            row) + getDigitSum(col) <= threshold and not visited[row][col]:
        return True
    return False


def getDigitSum(num):
    sum = 0
    while num > 0:
        sum += int(num % 10)
        num /= 10

    return sum


if __name__ == '__main__':
    print(MovingCount(18, 20, 20))
