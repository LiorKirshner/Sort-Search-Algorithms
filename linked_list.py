class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def __str__(self): #print
        pri = ""
        temp = self.head
        while temp:
            pri = (pri + str(temp.value) + " ")
            temp = temp.next
        return pri

    # הפונקציה מכניסה איבר חדש לתחילת הרשימה
    def push(self, value):
        new_node = Node(value)

        # אם הרשימה ריקה
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    # פונקציה מכניסה איבר לסוף הרשימה
    def append(self, value):
        new_node = Node(value)
        # אם הרשימה ריקה
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
        self.size += 1

    # הפונקציה מכניסה ערך לתוך מיקום (מתחילים מ1)
    def insert(self, position, value):
        new_node = Node(value)
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
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def search(self, value):
        if self.size < 1:
            return False
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def delete_by_value(self, value):
        if not self.search(value):
            return "value didn't show in the list"

        elif self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return "successes delete the head"

        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.value == value:
                    temp.next = temp.next.next
                    self.size -= 1
                    return "successes delete"
                temp = temp.next

            if temp.next.value == value:
                temp.next = None
                self.size -= 1
                return "successes delete the last"

    def delete_by_index(self, index):
        if self.size < index or index < 1:
            return "invalid index"

        if index == 1:
            self.head = self.head.next
            self.size -= 1
            return "successes delete the head"
        if index == self.size:
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1
        else:
            counter = 1
            temp = self.head
            for i in range(1, index-1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1
            return "successes delete"

    def bubble_sort(self):
        j = 0
        for i in range(0, self.size-1):
            x = self.head
            for j in range(0, self.size -1 -i):
                y = x.next
                if x.value > y.value:
                    x.value , y.value = y.value, x.value
                x = x.next

    def selection_sort(self):
        temp = self.head
        while temp :
            mini = temp
            x = temp.next
            while x:
                if mini.value > x.value:
                    mini = x
                x = x.next

            temp.value , mini.value = mini.value, temp.value
            temp = temp.next

    def reverse(self, head):

        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest

    def reverse2(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        # Returns the linked list in display format

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.value) + " ")
            temp = temp.next
        return linkedListStr








def main():

    my_linked_list = LinkedList()

    my_linked_list.append(10)
    my_linked_list.append(20)
    my_linked_list.append(30)
    my_linked_list.append(40)
    my_linked_list.append(50)

    print("Given linked list")
    print(my_linked_list)

    #my_linked_list.head = my_linked_list.reverse(my_linked_list.head)
    my_linked_list.reverse2()
    print("Reversed linked list")
    print(my_linked_list)



if __name__ == '__main__':
    main()
