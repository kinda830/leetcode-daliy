# encoding: utf-8
# a = input("please input a number:")
# print("hello world")


def test(str1, str2):
    result = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for i in range(len(str1) + 1):
        result[0][i] = i

    for i in range(len(str2) + 1):
        result[i][0] = i

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                result[i][j] = result[i - 1][j - 1]
            else:
                '''
                result[i - 1][j - 1] : 代表替换 str1[j] 和 str2[i]
                result[i][j-1] : 代表插入 str1[j]
                result[i-1][j] : 代表删除 str2[i]
                '''
                result[i][j] = min(result[i - 1][j - 1],
                                   min(result[i][j - 1], result[i - 1][j])) + 1

    return result[len(str2)][len(str1)]


print(test("horse", "ros"))
