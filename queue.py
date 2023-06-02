class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class Queue:
    def __init__(self, value=None):
        self.head = None
        self.endl = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        node_ = Node(value)
        if self.is_empty():
            self.head = node_
            self.endl = node_
        else:
            node_.previous = self.endl
            self.endl.next = node_
            self.endl = node_

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            elem = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.endl = None
            else:
                self.head.previous = None
            return elem

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __repr__(self):
        result = 'Queue('
        cur = self.head
        count = 0
        while cur:
            if count == 0:
                result += str(cur.value)
                count += 1
            else:
                result += ', ' + str(cur.value)
            cur = cur.next
        result += ')'
        return result

    def __copy__(self):
        new_queue = Queue()
        cur = self.head
        while cur:
            new_queue.enqueue(cur.value)
            cur = cur.next
        return new_queue