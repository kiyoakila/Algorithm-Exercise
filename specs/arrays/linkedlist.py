from os import curdir
from turtle import Turtle

from requests import head


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# linked list class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        current = self
        lenth = 0
        while current:
            lenth += 1
            current = current.next
        return lenth

    def hasCycle(self):
        if not self.head or not self.head.next:
            return False
        slow = self.head
        fast = self.head.next
        while fast is not None and fast.next is not None:
            if slow == fast or fast.next == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False


    # insertion
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            # append to the end of the list
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # deletion
    # But you cant delete the first element...
    # Treating the dummy head with the invariant that it is always pointing to the current correct answer 
    #  the dummy head, that will point to your final answer or list that you will return.
    def delete(self, data):
        dummy = Node("dummy")
        # initialize to point to the head
        dummy.next = self.head 
        p = dummy
        current = self.head
        # Because we created the dummy head we don't have to treat deleting the head of the original list any different from other elements in the list.
        while(current):
            if current.data == data:
                p.next = current.next
                return dummy.next
            p = current
            current = current.next
        # If we don't happen to find the item setting the dummy head to the original list makes it still point to the correct answer.
        return dummy.next

    # print the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
# LL.printLL()

LL.delete(4)
# print(val.data)
# LL.printLL()
LL.delete(3)
# print(val.data)
LL.printLL()