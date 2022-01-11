'''
@filename		:quick_sort.py
@Description	:快速排序
@Date			:2022/01/11 16:18:57
@Author      	:hjd
@version      	:1.0
'''


def quick_sort(numbers, start, end):
    if start < end:
        tmp = numbers[start]
        left, right = start, end

        while left < right:

            while left < right and numbers[right] >= tmp:
                right -= 1

            numbers[left] = numbers[right]
            while left < right and numbers[left] < tmp:
                left += 1

            numbers[right] = numbers[left]

        numbers[left] = tmp

        quick_sort(numbers, start, left - 1)
        quick_sort(numbers, left + 1, end)

    return numbers


if __name__ == "__main__":
    numbers = [1, 2, 7, 23, 54, 3, 5, 7, 21, 4]
    print(quick_sort(numbers, 0, len(numbers) - 1))
