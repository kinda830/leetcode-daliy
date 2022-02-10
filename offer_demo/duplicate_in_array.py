'''
@filename		:duplicateInArray.py
@Description	:查找一个数组中重复的数值
@Date			:2022/01/12 10:33:40
@Author      	:hjd
@version      	:1.0
'''


def duplicate_in_array(data):
    duplicate = []

    if data and len(data) > 0:
        for i in range(len(data)):
            if data[i] != i:
                if data[i] == data[data[i]]:
                    duplicate.append(data[i])
                else:
                    tem = data[i]
                    data[i], data[tem] = data[tem], data[i]
    return duplicate


if __name__ == '__main__':
    data = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate_in_array(data))
