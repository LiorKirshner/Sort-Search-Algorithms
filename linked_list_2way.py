class Node2way:

    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


class LinkedList2way:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # הפונקציה מכניסה איבר חדש לתחילת הרשימה
    def push(self, value):
        new_node = Node2way(value)

        # אם הרשימה ריקה
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # פונקציה מכניסה איבר לסוף הרשימה
    def append(self, value):
        new_node = Node2way(value)
        # אם הרשימה ריקה
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    # הפונקציה מכניסה ערך לתוך מיקום (מתחילים מ1)
    def insert(self, position, value):
        new_node = Node2way(value)
        if position < 1:
            print("ERROR -negative index")
        elif self.size < position - 1:
            print("ERROR - the list is too small")
        elif position == 1:
            self.push(value)
        elif self.size == position - 1:
            self.append(value)
        else:
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            temp.next.prev = new_node
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def search(self, value):
        if self.size < 1:
            return -1
        temp = self.head
        count = 1;
        while temp is not None:
            if temp.value == value:
                return count
            temp = temp.next
            count += 1
        return -1
    def search_by_index(self, index):
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        return temp

    def delete_by_value(self, value):
        index = self.search(value)
        self.delete_by_index(index)



    def delete_by_index(self, index):
        if self.size < index or index < 1:
            return "invalid index"

        if index == 1:
            self.head = self.head.next
            self.size -= 1
            return "successes delete the head"
        if index == self.size:
            temp = self.head
            for i in range(1, index - 1):
                temp = temp.next
            temp.next.next.prev == temp
            temp = temp.next
            temp.next = temp.next.next
            self.size -= 1
        else:
            counter = 1
            temp = self.head
            for i in range(1, index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1
            return "successes delete"







def main():
    # יצרנו רשימה
    my_linked_list = LinkedList2way()

    # נכניס איבר להתחלה
    my_linked_list.push(4545)
    my_linked_list.push(3)
    my_linked_list.push(343)

    my_linked_list.push(2)
    my_linked_list.push(4)

    my_linked_list.push(43)
    my_linked_list.push(45453)


    my_linked_list.print_list()
    print('-----')







if __name__ == '__main__':
    main()
