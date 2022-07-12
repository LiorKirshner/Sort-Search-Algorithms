class Node:
    def __init__(self, data):
        self.value = data
        self.parent = None
        self.right = None
        self.left = None
        self.high = 1


class AVL:
    def __init__(self):
        self.root = None

    def search_rec(self, root, data):
        if root.value == data or root.value is None:
            return root
        if root.value > data:
            return self.search_rec(root.left, data)
        else:
            return self.search_rec(root.right, data)

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp is not None:
                spy = temp
                if data < temp.value:
                    temp = temp.left
                else:
                    temp = temp.right
            new_node.parent = spy
            if data < spy.value:
                spy.left = new_node
            else:
                spy.right = new_node
        self.high_fix(new_node.parent)
        self.balance(new_node.parent)
        return new_node

    def balance(self, node):
        while node is not None:
            x = y = 0
            if node.left is not None:
                x = node.left.high

            if node.right is not None:
                y = node.right.high
            z = x - y

            #גובה לא תקין מימין
            if z <= -2:
                if node.right.right is not None:
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)

            #גובה לא תקין משמאל
            elif z >= 2:
                if node.left.left is not None:
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)

            node = node.parent

    def high_fix(self, node):
        while node is not None:
            if node.left is not None:
                x = node.left.high
            else:
                x = 0
            if node.right is not None:
                y = node.right.high
            else:
                y = 0
            node.high = max(x, y) + 1
            node = node.parent

    def left_rotate(self, node):
        y = node.right
        t = node.parent
        z = y.left

        y.parent = t
        y.left = node
        node.parent = y
        node.right = z
        if z is not None:
            z.parent = node
        if t is not None:
            if t.left == node:
                t.left = y
            else:
                t.right = y
        else:
            self.root = y
        self.high_fix(node)

    def right_rotate(self, node):
        y = node.left
        t = node.parent
        z = y.right

        y.parent = t
        y.right = node
        node.parent = y
        node.left = z
        if z is not None:
            z.parent = node
        if t is not None:
            if t.left == node:
                t.left = y
            else:
                t.right = y
        else:
            self.root = y
        self.high_fix(node)

    def pre_order_traversal(self, root, location):
        if root is not None:
            print(root.value, 'the high is', [root.high], 'and it\'s', location, end= ' ')
            if root.parent is not None:
                print('of (', root.parent.value, ')')
            else:
                print('')
            self.pre_order_traversal(root.left, 'left')
            self.pre_order_traversal(root.right, 'right')

    def sucessor(self, node):
        temp = node.right
        spy = temp
        while temp is not None:
            spy = temp
            temp = temp.left
        if spy is not None:
            return spy
        else:
            temp = node
            while temp.parent is not None and temp.parent.right == temp:
                temp = temp.parent
            return temp.parent

    def predecessor(self, node):
        temp = node.left
        spy = temp
        while temp is not None:
            spy = temp
            temp = temp.right
        if spy is not None:
            return spy
        else:
            temp = node
            while temp.parent is not None and temp.parent.left == temp:
                temp = temp.parent
            return temp.parent

    def delete(self, node):
        if node.right is None or node.left is None:
            y = node
        else:
            y = self.sucessor(node)
        t = y.parent
        if y.right is not None:
            x = y.right
        else:
            x = y.left
        if x is not None:
            x.parent = t

        if t is not None:
            if t.right == y:
                t.right = x
            else:
                t.left = x
        else:
            self.root = x
        if y != node:
            node.value = y.value
        y.parent = y.left = y.right is None
        if t is not None:
            self.high_fix(t)
            self.balance(t)


def main():
    Tree = AVL()

    Tree.insert(5)
    Tree.insert(6)
    Tree.insert(10)
    Tree.insert(7)
    Tree.insert(40)
    Tree.insert(30)
    Tree.insert(67)
    Tree.insert(32)
    Tree.insert(18)

    x = Tree.search_rec(Tree.root, 67)
    Tree.delete(x)

    Tree.insert(35)
    print(Tree.root.left.value)
    print(Tree.root.left.left.value)


    #Tree.pre_order_traversal(Tree.root, 'root')

if __name__ == '__main__':
    main()
