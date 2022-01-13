'''
@file        :find_target_sum_ways.py
@Description :
    给你一个整数数组 nums 和一个整数 target 。
    向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
    例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
    返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
@Date        :2022/01/12 21:21:41
@Author      :kinda
@version     :1.0
'''
import numpy as np


# 回溯解法
def find_target_sum_ways(numbers, target):
    count = 0

    def backtrack(i, sum, count):
        if i == len(numbers):
            if sum == target:
                count += 1
        else:
            count = backtrack(i + 1, sum + numbers[i], count)
            count = backtrack(i + 1, sum - numbers[i], count)
        return count

    count = backtrack(0, 0, count)

    return count


# 动态规划
def find_target_sum_ways2(numbers, target):
    sum = np.sum(numbers)
    neg = sum - target

    if neg % 2 == 0:
        neg = int(neg / 2)
        dp = []
        for _ in range(len(numbers) + 1):
            dp.append([0] * (neg + 1))

        dp[0][0] = 1

        for i in range(1, len(numbers) + 1):
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= numbers[i - 1]:
                    dp[i][j] += dp[i - 1][j - numbers[i - 1]]
        return dp[len(numbers)][neg]
    else:
        return 0


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3

    print(find_target_sum_ways(numbers, target))
    print(find_target_sum_ways2(numbers, target))
