'''
@Description:       :
@Date     :2021/12/23 21:33:53
@Author      :kinda
@version      :1.0
'''


def HasPath(matrix, sent):
    if matrix:
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        path_length = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if HasPathCore(matrix, i, j, sent, path_length, visited):
                    return True

        return False


def HasPathCore(matrix, row, col, sent, path_length, visited):
    if len(sent) == path_length:
        return True

    has_path = False
    if row >= 0 and row < len(matrix) and col >= 0 and col < len(
            matrix[0]) and matrix[row][col] == sent[path_length] and not visited[row][col]:
        path_length += 1
        visited[row][col] = True
        has_path = HasPathCore(
            matrix, row, col - 1, sent, path_length, visited) or HasPathCore(
                matrix, row - 1, col, sent, path_length, visited) or HasPathCore(
                    matrix, row, col + 1, sent, path_length, visited) or HasPathCore(
                        matrix, row + 1, col, sent, path_length, visited)

        if not has_path:
            path_length -= 1
            visited[row][col] = False

    return has_path


if __name__ == '__main__':
    matrix = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]

    sent = 'bfce'

    print(HasPath(matrix, sent))
