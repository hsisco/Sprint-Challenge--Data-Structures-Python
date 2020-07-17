class RingBuffer:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.storage = []
        self.curr = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.curr = (self.curr +1) % self.capacity
            self.storage[self.curr] = item
        else:
            self.storage.append(item)

    def get(self):
        return self.storage