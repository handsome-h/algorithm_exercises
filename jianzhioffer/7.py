"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []


class CQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def appendTail(self, val):
        self.stack1.push(val)

    def deleteHead(self):
        # print(self.stack1.size())
        while not self.stack1.isEmpty():
            tmp = self.stack1.pop()
            # print(tmp)
            self.stack2.push(tmp)
        self.stack2.pop()

    def show(self):
        while not self.stack1.isEmpty():
            tmp = self.stack1.pop()
            self.stack2.push(tmp)

        while not self.stack2.isEmpty():
            print(self.stack2.pop())


q = CQueue()
q.appendTail(2)
q.appendTail(3)
q.appendTail(1)
q.appendTail(4)
q.deleteHead()
q.deleteHead()
q.show()
