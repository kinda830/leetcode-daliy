'''
@file        :VerifySquenceOfBST.py
@Description :
@Date        :2022/01/05 23:06:08
@Author      :kinda
@version     :1.0
'''


def verify_of_BST(numbers):
    if numbers:
        root = numbers[-1]

        i = 0
        for i in range(len(numbers) - 1):
            if numbers[i] > root:
                break

        j = i
        for j in range(i, len(numbers) - 1):
            if numbers[j] < root:
                return False

        left = True
        if i > 0:
            left = verify_of_BST(numbers[:i])

        right = True
        if i < len(numbers) - 1:
            right = verify_of_BST(numbers[i:len(numbers) - 1])

        return left and right

    return False


if __name__ == "__main__":
    a = [5, 7, 6, 9, 11, 10, 8]
    print(verify_of_BST(a))
