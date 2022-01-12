'''
@filename		:clone_sibling_node.py
@Description	:复制复杂链表
@Date			:2022/01/12 11:01:21
@Author      	:hjd
@version      	:1.0
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.sibling = None


def clone_node(head):
    p_head = head

    while p_head:
        clone_node = Node(p_head.value)
        clone_node.next = p_head.next
        p_head.next = clone_node
        p_head = clone_node.next

    return head


def connect_sibling_node(head):
    p_node = head
    while p_node:
        if p_node.sibling:
            p_node.next.sibling = p_node.sibling.next

        p_node = p_node.next

    return head


def reconnect_node(head):
    p_node = head
    p_clone_head = None
    p_clone_node = None

    if p_node:
        p_clone_head = p_node.next
        p_clone_node = p_node.next
        p_node = p_clone_node.next

    while p_node:
        p_clone_node.next = p_node.next
        p_clone_node = p_clone_node.next
        p_node.next = p_clone_node.next
        p_node = p_node.next

    return p_clone_head


def clone(head):
    head = clone_node(head)
    head = connect_sibling_node(head)
    head = reconnect_node(head)

    while head:
        print(head.value)
        head = head.next


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.sibling = node3
node2.sibling = node5
node4.sibling = node2

clone(node1)
