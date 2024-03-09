"""
Python Data Structure Stack Class Explaination
 Mohammed Bilal

Inside of a Class. Function is called Method. There is No difference as such
"""


class Stack:

    # init is a constructor
    def __init__(self):
        self.stackitems = []

    def peek(self):
        return self.stackitems[-1]

    def pop(self):
        return self.stackitems.pop()

    # Need to pass some item to push to push tose item to stack
    def push(self, stackitems):
        self.stackitems.append(stackitems)

    def is_empty(self):
        # return len(self.stackitems) == 0
        return not self.stackitems

    def size(self):
        return len(self.stackitems)

    # it is generally a print statement to inspect the stack
    def __str__(self):
        return str(self.stackitems)


if __name__ == '__main__':
    s = Stack()

    print(s)
    print("this is from stack file")

    s.push(1)
    s.push("Robert")
    s.push(3.145)

    s.push([1, 2, 3])

    print(s)

    s.pop()
    print(s)

    print(s.peek(1))

    print(s.size())

    print(s.is_empty())

    s.pop()
    s.pop()
    s.pop()

    print(s.is_empty())
