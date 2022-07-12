class Node:

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None


#ממויין תמיד
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)


def pre_order_traversal(root):
    if root is not None:
        print(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value)


def print_leaf(root):
    if root is None:
        return "value dont exist"
    else:
        return root.value


def search_rec(root, data):
    if root is None or root.value == data:
        return root

    if root.value > data:
        return search_rec(root.left, data)
    else:
        return search_rec(root.right, data)


def search(root, data):
    temp = root
    while temp is not None and temp.value != data:
        if temp.value > data:
            temp = temp.left
        else:
            temp = temp.right
    return temp


def find_closer(self, v):

    low_bound = high_bound = None
    searcher = self.root
    while searcher is not None:
        if searcher.value > v:
            high_bound = searcher
            searcher = searcher.left
        else:
            low_bound = searcher
            searcher = searcher.right

    if high_bound is None:
        return low_bound
    elif low_bound is None:
        return high_bound
    elif high_bound.value - v < v - low_bound.value:
        return high_bound
    else:
        return low_bound


def find_minimum(root):
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp


def find_maximum(root):
    temp = root
    while temp.right is not None:
        temp = temp.right
    return temp


#עוקב
def successor(root):
    if root.right is not None:
        return find_minimum(root.right)
    else:
        temp = root
        father = root.parent
        while father is not None and father.right == temp:
            father = father.parent
            temp = temp.parent
        return father


#קודם
def predecessor(v):
    if v.left is not None:
        return find_maximum(v.left)
    else:
        temp = v
        father = v.parent
        while father is not None and father.left == temp:
            father = father.parent
            temp = temp.parent
        return father


def insert(root, data):
    new_node = Node(data)
    if root is None:
        root = new_node
    else:
        temp = root
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


def delete(root, v):

    #נדע איזה קודקוד להסיר
    if v.left is None or v.right is None:
        y = v
    else:
        y = successor(v)

    #אם יש בן 1
    if y.left is not None:
        ySon = y.left
    else:
        ySon = y.right

    if ySon is not None:
        ySon.parent = y.parent

    if y.parent is None:
        root = ySon
    else:
        if y == y.parent.left:
            y.parent.left = ySon
        else:
            y.parent.right = ySon

    if y != v:
        v.data = y.data

    return y


def main():
    root = Node(100)
    V2 = Node(80)
    V3 = Node(200)
    V4 = Node(70)
    V5 = Node(90)
    V6 = Node(150)
    V7 = Node(75)
    V8 = Node(170)

    root.left = V2
    root.right = V3
    V2.parent = root
    V2.parent = root
    V2.left = V4
    V4.parent = V2
    V2.right = V5
    V5.parent = V2
    V3.left = V6
    V3.right = V4
    V4.parent = V3
    V6.parent = V3
    V4.right = V7
    V7.parent = V4
    V6.left = V8
    V8.parent = V6


    #in_order_traversal(root)
    ans = search(root, 730)
    print(predecessor(V7).value)
   # print(print_leaf(ans))
    #print(print_leaf(find_minimum(root)))
    #print(print_leaf(successor(V2)))
    #print(print_leaf(predecessor(root)))

if __name__ == '__main__':
    main()