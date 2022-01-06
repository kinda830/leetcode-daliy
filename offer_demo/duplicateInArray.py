'''
@Description:       :
@Date     :2021/12/12 15:11:42
@Author      :xia
@version      :1.0
'''


def duplicate_in_array(data):
    duplicate = []

    if data and len(data) > 0:
        for i in range(len(data)):
            if data[i] == i:
                continue
            else:
                if data[i] == data[data[i]]:
                    duplicate.append(data[i])
                else:
                    tem = data[i]
                    data[i], data[tem] = data[tem], data[i]
    return duplicate


if __name__ == '__main__':
    data = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate_in_array(data))
