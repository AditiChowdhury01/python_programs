class stack:
    def __init__(self):
        self.values = []
    def push(self,item):
        self.values.append(item)
    def pop(self):
        return self.values.pop()
    def size(self):
        return len(self.values)

s = stack()
s.push(20)
s.push(30)
s.push(40)
s.push(10)
print(s.values)
s.pop()
s.pop()
s.pop()
print(s.values)
print(s.size())