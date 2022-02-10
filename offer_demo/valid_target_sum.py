'''
@file        :valid_target_sum.py
@Description :判断一个数组中是否存在几个数据的和为目标值
@Date        :2022/01/14 22:23:46
@Author      :kinda
@version     :1.0
'''


def test(numbers, target):

    # flag = False

    def backtrack(sum, index):
        if sum == target:
            flag = True
            return flag
        for i in range(index, len(numbers)):
            sum += numbers[i]
            flag = backtrack(sum, i + 1)
            if flag:
                return flag
            sum -= numbers[i]

        return False

    return backtrack(0, 0)


if __name__ == "__main__":
    numbers = [4, 1, 2, 4, 7]
    print(test(numbers, 13))
