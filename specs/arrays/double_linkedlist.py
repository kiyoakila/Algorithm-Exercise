from email import header
from msilib.schema import SelfReg
from os import preadv
from queue import Empty


class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_val', '_prev', '_next'
        def __init__(self, val, prev, next):
            self._val = val
            self._prev = prev
            self._next = next

    def __init__(self):
        # link the header and the trailer
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def _insert_between(self, val, pred, succ):
        new_node = self._Node(val, pred, succ)
        pred._next = new_node
        succ._prev = new_node
        self._length += 1
        return new_node

    def _delete_node(self, node):
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._length -= 1
        ans = node._val
        # help garbage collection; deprecate node
        node._val, node._prev, node._next = None
        return ans

    
# --- Double-ended Queue --- #
class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self._header._next._val

    def last(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self._trailer._prev._val

    def insert_first(self, val):
        self._insert_between(val, self._header, self._header._next)

    def insert_last(self, val):
        self._insert_between(val, self._trailer._prev, self._trailer)
        
    def delete_first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self._delete_node(self._header._next)

    def delete_first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self._delete_node(self._trailer._prev)
    





