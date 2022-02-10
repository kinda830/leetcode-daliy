'''
@filename		:find_number_index_in_list.py
@Description	:
    给定一个按照升序排列的整数数组 nums, 和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target, 返回 [-1, -1]。
@Date			:2022/02/10 15:26:19
@Author      	:hjd
@version      	:1.0
'''


def binary_search(numbers, target, lower):
    left, right, ans = 0, len(numbers) - 1, len(numbers)

    while left < right:
        mid = int((left + right) / 2)
        if numbers[mid] > target or (lower and numbers[mid] >= target):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    return ans


def find_number_index_in_list(numbers, target):
    left_idx = binary_search(numbers, target, True)
    right_idx = binary_search(numbers, target, False) - 1

    if left_idx <= right_idx and right_idx < len(numbers) and numbers[left_idx] == target and numbers[right_idx] == target:
        return [left_idx, right_idx]
    else:
        return [-1, -1]


if __name__ == "__main__":
    numbers = [3, 4, 5, 6, 6, 6, 7, 7, 8, 8, 8, 10]
    target = 7
    print(find_number_index_in_list(numbers, target))
