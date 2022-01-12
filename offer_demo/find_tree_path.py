'''
@filename		:find_tree_path.py
@Description	:在二叉树中寻找路径之和为指定的一条路径
@Date			:2022/01/12 11:03:09
@Author      	:hjd
@version      	:1.0
'''


def find_tree_path(tree, number, path, current_num):
    if tree:
        current_num += tree.value
        path.append(str(tree.value))
        is_leaf = tree.left is None and tree.right is None
        if is_leaf and current_num == number:
            print("path is found: {}".format("-".join(path)))

        if tree.left:
            find_tree_path(tree.left, number, path, current_num)

        if tree.right:
            find_tree_path(tree.right, number, path, current_num)

        path.pop()


def find_path(tree, number):
    path = []
    current_num = 0

    find_tree_path(tree, number, path, current_num)


class Tree():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


tree1 = Tree(10)
tree2 = Tree(5)
tree3 = Tree(12)
tree4 = Tree(4)
tree5 = Tree(7)

tree1.left = tree2
tree1.right = tree3

tree2.left = tree4
tree2.right = tree5

find_path(tree1, 22)
