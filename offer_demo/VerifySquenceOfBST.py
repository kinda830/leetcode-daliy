'''
@file        :VerifySquenceOfBST.py
@Description :
@Date        :2022/01/05 23:06:08
@Author      :kinda
@version     :1.0
'''


def verify_squence_bst(sequence, length):

    if sequence:
        root = sequence[length - 1]
        i = 0
        for i in range(length - 1):
            if sequence[i] > root:
                break

        j = i
        for j in range(length - 1):
            if sequence[j] < root:
                return False

        left = True
        if i > 0:
            left = verify_squence_bst(sequence[0:i], i)

        right = True
        if i < length - 1:
            right = verify_squence_bst(sequence[i:j], j - i)

        return left and right
    return False


if __name__ == "__main__":
    a = [5, 7, 6, 9, 11, 10, 8]
    print(verify_squence_bst(a, len(a)))
