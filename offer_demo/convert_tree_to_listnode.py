'''
@filename		:convert_tree_to_listnode.py
@Description	:二叉搜索树转换为排序后的双向链路
@Date			:2022/01/07 11:49:24
@Author      	:hjd
@version      	:1.0
'''


class Tree():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def covert(tree):
    last_node = None

    last_node = convert_node(tree, last_node)

    head_list = last_node

    while head_list and head_list.left:
        head_list = head_list.left

    return head_list


def convert_node(tree, last_node):

    if tree:
        current_node = tree

        if current_node.left:
            last_node = convert_node(current_node.left, last_node)

        current_node.left = last_node

        if last_node:
            last_node.right = current_node
        
        last_node = current_node

        if current_node.right:
            last_node = convert_node(current_node.right, last_node)
        
        return last_node
    return None


tree1 = Tree(10)
tree2 = Tree(6)
tree3 = Tree(14)
tree4 = Tree(4)
tree5 = Tree(8)
tree6 = Tree(12)
tree7 = Tree(16)

tree1.left = tree2
tree1.right = tree3

tree2.left = tree4
tree2.right = tree5

tree3.left = tree6
tree3.right = tree7

p_head = covert(tree1)

while p_head:
    print(p_head.value)
    p_head = p_head.right
