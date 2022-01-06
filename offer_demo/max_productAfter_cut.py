'''
@file        :max_productAfter_cut.py
@Description:
@Date     :2021/12/25 16:15:29
@Author      :kinda
@version      :1.0
'''


def max_product_after_cut(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    products = [0] * (length + 1)

    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    max_num = 0
    for i in range(4, length + 1):
        max_num = 0
        for j in range(1, int(i / 2) + 1):
            product = products[j] * products[i - j]
            products[i] = max(max_num, product)

    max_num = products[length]

    return max_num


if __name__ == "__main__":
    print(max_product_after_cut(5))
