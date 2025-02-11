from functools import cmp_to_key

class PriorityQueue:
    def __init__(self, f):
        self._data = []
        self.f = f

        ##############################
        ### initialize an empty list
        ### set function f to self
        ### write code here
        ##############################
        pass

    def push(self, val):
        self._data.append(val)
        self._data = sorted(self._data, key=cmp_to_key(self.f), reverse=True)
        ##############################
        ### push new values into the list
        ### sort list in descending order based on self.f
        ### write code here
        ##############################
        pass

    def get(self, idx):
        return self._data(idx)
        ##############################
        ### get values by index
        ### write code here
        ##############################
        pass

    def __len__(self):
        return len(self._data)
        ##############################
        ### return length of queue
        ### write code here
        ##############################
        pass
        
    def pop(self):
        return self._data.pop(0)
        ##############################
        ### pop the first element in the list
        ### write code here
        ##############################
        pass

queue = PriorityQueue(lambda a, b: b - a) 

queue.push(4)
queue.push(5)
queue.push(2)
queue.push(7)

assert queue._data == [2, 4, 5, 7]

queue.push(1)

assert queue._data == [1, 2, 4, 5, 7]