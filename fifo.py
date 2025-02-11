class Fifo:
    def __init__(self):
        self._data = []
        pass
    def push(self, val):
        self._data.append(val)
        pass
    def get(self, idx):
        return self._data[idx]
        pass
    def __len__(self):
        return len(self._data)
        pass
    def pop(self):
        return self._data.pop(0)
        pass

d = Fifo()
d.push(4)
d.push(5)

d.pop()
a = d.pop()

assert a == 5 and len(d) == 0
