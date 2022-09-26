class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        return self.stack1

    def pop(self) -> int:
        if len(self.stack1) == 0:
            return 'null'
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return temp

    def peek(self) -> int:
        if len(self.stack1) == 0:
            return 'null'
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        temp = self.stack2[-1]
       
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return temp

    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False

# example test case
m = MyQueue()
print(m)
print(m.push(1))
print(m.push(2))
print(m.push(5))
print('peek', m.peek())
print('push',m.push(3))
print(m.pop())
print(m.peek())
print(m.empty())
