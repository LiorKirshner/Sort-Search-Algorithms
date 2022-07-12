class Stack:

    def __init__(self):
        self.top = 0
        self.st = []

    def is_empty(self):
        return self.top == 0

    def push(self, value):
        self.st.append(value)
        self.top += 1

    def pop(self):
        if not self.is_empty():
            x = self.st.pop()
            self.top -= 1
            return x

    def peek(self):
        return self.st[self.top-1]

    def stack_sort(self):
        tempStack = Stack()
        while not self.is_empty():
            x = self.pop()
            while not tempStack.is_empty() and tempStack.peek() > x :
                a = tempStack.pop()
                self.push(a)
            tempStack.push(x)
        self.st = tempStack.st



def secret(some_string):
        st = Stack()
        ans = ""
        for letter in some_string:
            if 'a' <= letter <= 'z':
                st.push(letter)
            elif letter == '*':
                a = st.pop()
                ans += a
        return ans


def main():
    stack1 = Stack()

    stack1.push(5)
    stack1.push(7)
    stack1.push(8)
    stack1.push(4544)
    stack1.push(3)
    stack1.push(65)
    stack1.push(1)


    print(secret("eaTGi*rs**Y**l%*$"))

    print(stack1.st)
    stack1.stack_sort()
    print(stack1.st)


if __name__ == '__main__':
    main()