'''
@filename		:max_productAfter_cut.py
@Description	:给你一根长度为n的绳子，请把绳子剪成m段(m和n都是整数，n>1并且m>1)， 每段绳子的长度记为k[0],k[1],...,k[m]. 请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
@Date			:2022/01/12 10:41:36
@Author      	:hjd
@version      	:1.0
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
    print(max_product_after_cut(10))
