class MaxQueue:

    def __init__(self):
        self.data = []
        self.max_vals = []

    def max_value(self) -> int:
        if not self.data:
            return -1
        return self.max_vals[-1]

    def push_back(self, value: int) -> None:
        self.data.append(value)
        if not self.max_vals or self.max_vals[-1] <= value:
            self.max_vals.append(value)

    def pop_front(self) -> int:
        if not self.data:
            return -1

        value = self.data.pop(0)
        if value == self.max_vals[0]:
            self.max_vals.pop(0)

        return value


# Your MaxQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MaxQueue()
    param_1 = obj.max_value()
    obj.push_back(1)
    param_3 = obj.pop_front()
