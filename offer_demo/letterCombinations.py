'''
@filename		:letterCombinations.py
@Description	:给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
@Date			:2022/01/11 19:13:52
@Author      	:hjd
@version      	:1.0
'''


def letter_combination(numbers):
    char_num = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []
    combination = []

    def backtrack(index):
        if index == len(numbers):
            result.append("".join(combination))
        else:
            number = numbers[index]
            for letter in char_num[number]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()

    backtrack(0)

    return result

if __name__ == "__main__":
    s = "23"
    print(letter_combination(s))
