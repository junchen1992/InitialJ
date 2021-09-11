"""用两个stack实现一个queue."""

#coding=utf-8
from collections import deque


class Queue:

    """A queue implemented with two stacks."""

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

        self.is_reversed = False

    def push(self, x):
        """Push a new element to the end of queue."""
        # Swap stack
        if self.is_reversed:
            empty_stack, data_stack = self.stack1, self.stack2
            if self.stack1:
                empty_stack, data_stack = self.stack2, self.stack1
            while data_stack:
                empty_stack.append(data_stack.pop())

        if self.stack2:
            self.stack2.append(x)
        else:
            self.stack1.append(x)

    def poll(self):
        """Retrieve the first element in queue."""
        if not self.stack1 and not self.stack2:
            raise Exception('Empty queue!')

        empty_stack, data_stack = self.stack1, self.stack2
        if self.stack1:
            empty_stack, data_stack = self.stack2, self.stack1

        if self.is_reversed:
            return data_stack.pop()
        else:
            while data_stack:
                empty_stack.append(data_stack.pop())
            self.is_reversed = not self.is_reversed
            return empty_stack.pop()
