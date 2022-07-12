class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = None

class BRbinary_tree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        y = node.right
        z = y.left
        t = node.parent
        if z is not None:
            z.parent = node
        node.parent = y
        y.parent = t
        node.right = z
        y.left = node
        if t is not None:
            if t.right == node:
                t.right = y
            else:
                t.left = y
        else:
            self.root = node.parent

    def right_rotate(self, node):
        y = node.left
        z = y.right
        t = node.parent

        if z is not None:
            z.parent = node
        node.left = z

        node.parent = y
        y.right= node

        y.parent = t
        if t is not None:
            if t.right == node:
                t.right = y
            else:
                t.left = y
        else:
            self.root = node.parent

    def insert(self, v):
        node = self.insert_before(v)
        node.color = 'red'

        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y is not None and y.color == 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                elif y is None or y.color == 'black':
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                        node.parent.color = 'black'
                        node.parent.parent.color = 'red'
                        self.right_rotate(node.parent.parent)
                    else:
                        n = node.parent.parent
                        self.right_rotate(n)
                        n.parent.color = 'black'
                        n.color = 'red'
            else:
                y = node.parent.parent.left
                if y is not None and y.color == 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                elif y is None or y.color == 'black':
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                        node.parent.color = 'black'
                        node.parent.parent.color = 'red'
                        self.left_rotate(node.parent.parent)
                    else:
                        n = node.parent.parent
                        self.left_rotate(n)
                        n.parent.color = 'black'
                        n.color = 'red'
        self.root.color = 'black'



    def insert2help(self,data):
        new_node = Node(data)
        new_node.color = 'red'
        if self.root is None:
            self.root = new_node
            return new_node
        else:
            temp = self.head
            while temp:
                spy = temp
                if temp.value > data:
                    temp = temp.left
                else:
                    temp = temp.right

            new_node.parent = spy
            if data < spy.value:
                spy.left = new_node
            else:
                spy.right = new_node
            return new_node


    def insert2(self, data):
        node = self.insert2help(data)

        if self.root is None:
            self.root = node
            node.color = 'black'
            return node

        while node != self.root and node.parent.color == 'red':
            p = node.parent
            while p.parent:
                if p.parent.left == p:
                    u = p.parent.right
                else:
                    u = p.parent.left
            if u.color == 'red':
                u.color = p.color = 'black'














    def rec_search(self, root, data):
        if root.value == data or root is None:
            return root
        if root.value > data:
            return self.rec_search(root.left, data)
        else:
            return self.rec_search(root.right, data)

    def search(self, data):
        temp = self.root
        while temp is not None and temp.value != data:
            if temp.value > data:
                temp = temp.left
            else:
                temp = temp.right
        return temp

    def insert_before(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            spy = None
            while temp is not None:
                spy = temp
                if temp.value > data:
                    temp = temp.left
                else:
                    temp = temp.right
            if data < spy.value:
                spy.left = new_node
            else:
                spy.right = new_node
            new_node.parent = spy
        return new_node

    def find_minimum(self, temp):
        while temp.left is not None:
            temp = temp.left
        return temp

    def find_maximum(self, temp):
        while temp.right is not None:
            temp = temp.right
        return temp

    def successor(self, node):
        if node.right is not None:
            return self.find_minimum(node.right)
        else:
            p = node.parent
            while p is not None and p.right == node:
                p = p.parent
                node = node.parent
            return p

    def predecessor(self, node):
        if node.left is not None:
            return self.find_maximum(node.left)
        else:
            p = node.parent
            while p is not None and p.left == node:
                p = p.parent
                node = node.parent
            return p

    def in_order_traversal(self, v, location):
        if v is not None:
            self.in_order_traversal(v.left, 'left')
            print(v.value, '[', v.color, ']', 'is', location, end = '')
            if v != self.root:
                print(' of', '(', v.parent.value, ')')
            else:
                print('')
            self.in_order_traversal(v.right, 'right')

    def pre_order_traversal(self, v, location):
        if v is not None:
            print(v.value, '[', v.color, ']', 'is', location, end='')
            if v != self.root:
                print('(', v.parent.value, ')')
            else:
                print('')
            self.pre_order_traversal(v.left, 'left')
            self.pre_order_traversal(v.right, 'right')

    def post_order_traversal(self, v, location):
        if v is not None:
            self.post_order_traversal(v.left, 'left')
            self.post_order_traversal(v.right, 'right')
            print(v.value, '[', v.color, ']', 'is', location, end='')
            if v != self.root:
                print('(', v.parent.value, ')')
            else:
                print('')

    def delete(self, node):
        if node.left is None or node.right is None:
            y = node
        else:
            y = self.successor(node)
        f = y.parent
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y != node:
            node.value = y.value
        y.parent = y.left = y.right = None
        self.delete_help(y, x, f)
        return y

    def delete_help(self, z, b, a):
        if z.color == 'black' and a is not None:
            if b == a.left:
                c = a.right
                if c is not None:
                    d = c.left
                    e = c.right
            else:
                c = a.left
                if c is not None:
                    e = c.left
                    d = c.right
            if b is None or b.color == 'black':
                if c is not None and c.color == 'black':
                    if e is not None and e.color == 'red':
                        if c == a.right:
                            self.left_rotate(a)
                            c.color = a.color
                            a.color = 'black'
                            e.color = 'black'
                        else:
                            self.right_rotate(a)
                            c.color = a.color
                            a.color = 'black'
                            e.color = 'black'
                    elif e is None or e.color == 'black':
                        if d is not None and d.color == 'red':
                            if d == c.left:
                                self.right_rotate(c)
                            else:
                                self.left_rotate(c)
                            d.color = 'black'
                            c.color = 'red'
                            if d == a.right:
                                self.left_rotate(a)
                            else:
                                self.right_rotate(a)
                        elif d is None or d.color == 'black':
                            if a.color == 'red':
                                a.color = 'black'
                                c.color = 'red'
                            else:
                                c.color = 'red'
                                self.delete_help(z, a, a.parent)
                elif c is not None and c.color == 'red':
                    if c == a.right:
                        self.left_rotate(a)
                    else:
                        self.right_rotate(a)
                    c.color = 'black'
                    a.color = 'red'
                    self.delete_help(z, b, a)
                else:
                    if a.color == 'red':
                        a.color = 'black'
                    else:
                        self.delete_help(z, a, a.parent)
            else:
                b.color = 'black'

def main():
    tree = BRbinary_tree()
    tree.insert(29)
    tree.insert(23)
    tree.insert(35)
    tree.insert(17)
    tree.insert(19)
    tree.insert(28)
    tree.insert(1)
    tree.insert(0)
    tree.insert(24)
    tree.insert(33)
    tree.insert(31)
    tree.insert(37)
    x = tree.search(1)
    tree.delete(x)
    tree.pre_order_traversal(tree.root, 'root')


if __name__ == '__main__':
    main()