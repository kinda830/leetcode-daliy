'''
@filename		:tree_demo.py
@Description	:从上到下打印二叉树
@Date			:2022/01/12 10:59:39
@Author      	:hjd
@version      	:1.0
'''
from utils import Queue


class Tree():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def print_two_tree(tree):

    if tree:
        queue = Queue()
        result = []
        queue.en_queue(tree)
        while queue.size():
            item = queue.de_queue()
            if item:
                result.append(item.value)
                if item.left:
                    queue.en_queue(item.left)
                if item.right:
                    queue.en_queue(item.right)
        return result


tree1 = Tree(8)
tree2 = Tree(6)
tree3 = Tree(10)
tree4 = Tree(5)
tree5 = Tree(7)
tree6 = Tree(9)
tree7 = Tree(11)

tree1.left = tree2
tree1.right = tree3

tree2.left = tree4
tree2.right = tree5

tree3.left = tree6
tree3.right = tree7

print(print_two_tree(tree1))
