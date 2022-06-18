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

    # cycle detection
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


# --- Linked Stack --- #
# all operations has O(1) time complexity
# align the top of the stack with the head of the list
class LinkedStack:
    # nested node class
    class _Node:
        __slots__ = '_val', '_next'

        def __init__(self, val, next):
            self._val = val
            self._next = next
    # stack method

    def __init__(self):
        self._head = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def push(self, val):
        self._head = self._Node(val, self._head)
        self._length += 1

    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self._head._val

    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        old_top = self._head
        self._head = self._head._next
        self._length -= 1
        return old_top._val
    
# --- Linked Queue --- #
# all operations has O(1) time complexity
# align the front of the stack with the head of the list, since we can't effectively dequeue from the tail of the singlely linkede list

class LinkedQueue:
    class _Node:
        __slots__ = '_val', '_next'
        def __init__(self, val, next):
            self._val = val
            self._next = next
    # queue methods
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self._head._val

    def enqueue(self, val):
        new_node = self._Node(val, self._tail)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._length += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")
        old_head = self._head
        self._head = self._head._next                
        self._length -= 1
        if self.is_empty():
            self._tail = None
        return old_head._val

    def rotate(self):
        """ dequeue the first element and insert at the back of the queue"""
        front = self.dequeue()
        self.enqueue(front)

# --- Circular Queue --- #
# implemented with circular singlely linked list
class CircularQueue:
    class _Node:
        __slots__ = '_val', '_next'
        def __init__(self, val, next):
            self._val = val
            self._next = next
    # queue methods
    def __init__(self):
        # head is substuted by tail.next
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        head = self._tail._next
        return head._val

    def enqueue(self, val):
        new_node = self._Node(val, self._tail)
        if self.is_empty():
            new_node._next = new_node
        else:
            head = self._tail._next
            new_node._next = head
            self._tail._next = new_node
        self._tail = new_node
        self._length += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")
        old_head = self._tail._next
        if self._length == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next                
        self._length -= 1
        return old_head._val

    def rotate(self):
        self._tail = self._tail._next
