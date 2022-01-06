'''
@file        :HasSubTree.py
@Description: 在一棵二叉树上寻找是否存在另一个小的二叉树的子树
@Date     :2021/12/26 22:02:33
@Author      :kinda
@version      :1.0
'''


def has_sub_tree(tree1, tree2):
    result = False
    if tree1 and tree2:
        if tree1.value == tree2.value:
            result = does_tree1_have_tree2(tree1, tree2)
        if not result:
            result = has_sub_tree(tree1.left, tree2)
        if not result:
            result = has_sub_tree(tree1.right, tree2)

    return result


def does_tree1_have_tree2(tree1, tree2):
    result = False
    if tree1 and tree2:
        if tree1.value != tree2.value:
            return False

        return does_tree1_have_tree2(tree1.left, tree2.left) and does_tree1_have_tree2(tree1.right, tree2.right)

    return result
