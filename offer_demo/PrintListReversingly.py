'''
@Description:       :
@Date     :2021/12/15 21:44:56
@Author      :kinda
@version      :1.0
'''


class Tree(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def PrintListReversingly(head):
    '''
    第一种思路: 递归遍历链表，并在最后的节点打印数据并返回上一层调用
    第二种思路: 遍历链表并把数据存放到栈中，遍历完后再访问并打印栈的数据
    '''
    if head:
        if head.next:
            PrintListReversingly(head.next)
        print(head.value)


if __name__ == '__main__':
    one = Tree(0)
    old = one
    for i in range(1, 10):
        tmp = Tree(i)
        old.next = tmp
        old = tmp

    PrintListReversingly(one)
