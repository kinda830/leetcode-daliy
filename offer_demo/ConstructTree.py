'''
@Description:       :
@Date     :2021/12/15 22:33:17
@Author      :kinda
@version      :1.0
'''


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct_tree(pre_order, in_order):
    if pre_order and in_order and len(pre_order) == len(in_order):
        root = TreeNode(pre_order[0])
        if len(pre_order) == 1:
            return root
        else:
            index = 0
            while in_order[index] != pre_order[0]:
                index += 1
            if index > 0:
                root.left = construct_tree(pre_order[1:index + 1], in_order[:index])
            if index < len(in_order):
                root.right = construct_tree(pre_order[index + 1:], in_order[index + 1:])
            return root


if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]

    tree = construct_tree(pre_order, in_order)
    print("lll")
