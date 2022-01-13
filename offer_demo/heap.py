'''
@filename		:heap.py
@Description	:堆的基础类
@Date			:2022/01/13 16:11:51
@Author      	:hjd
@version      	:1.0
'''


class MaxHeap():
    def __init__(self) -> None:
        self.data = []

    def build(self, arr):
        if len(arr) == 1:
            self.data = arr
        else:
            n = (len(arr) - 2) / 2

            while n >= 0:
                self.max_heapify(arr, n)
                n -= 1

    def pop(self):
        num = self.data[0]
        self.data[0] = self.data.pop()

        self._max_heapify(self.data, 0)
        return num

    def _max_heapify(self, arr, root):
        if root > len(arr):
            return

        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < len(arr) and arr[left] < arr[largest]:
            largest = left

        if right < len(arr) and arr[right] < arr[largest]:
            largest = right

        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]

            self.max_heapify(arr, root)
