'''
@filename		:serialize_tree.py
@Description	:二叉树序列化
@Date			:2022/01/10 10:53:59
@Author      	:hjd
@version      	:1.0
'''

class Tree():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def serialize_tree(tree):
    result = []

    def serialize(tree):
        if not tree:
            result.append('$')
        else:
            result.append(tree.value)
            serialize(tree.left)
            serialize(tree.right)

def deserialize_tree(tree_list):
    if tree_list:
        root = Tree(tree_list[0])
        current = root
        pre_node = root
        is_left = True
        for number in tree_list[1:]:
            if number != "$":
                if is_left:
                    current.left = Tree(number)
                else:
                    pass
            else:
                if is_left:
                    is_left = False
                else:
                    current = pre_node
            


