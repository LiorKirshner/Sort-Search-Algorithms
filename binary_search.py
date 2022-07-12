"""
binary_search(my_list, low, high, value)

my_list - רשימת המספרים
low - גבול חיפוש תחתון
high - גבול חיפוש עליון
value - ערך שרוצים להכניס לרשימה

הפונקציה מחזירה את המיקום שצריך להכניס לתוכו את הערך value
"""




def binary_search(my_list, low, high, value):
    if low == high:
        if my_list[high] >= value:
            return high
        else:
            return high + 1
    if low > high:
        return low

    mid = (low + high) // 2
    if my_list[mid] == value:
        return mid
    elif my_list[mid] < value:
        return binary_search(my_list, mid + 1, high, value)
    else:
        return binary_search(my_list, low, mid - 1, value)








# Q1 - test
def binary_search(my_list, low, high, value):

    if low == high:
        if my_list[high] > value:
            return high
        else:
            return high + 1

    if low > high:
        return low

    mid = (low + high) // 2

    if my_list[mid] < value:
        return binary_search(my_list, mid + 1, high, value)
    elif my_list[mid] > value:
        return binary_search(my_list, low, mid - 1, value)
    else:
        return mid


def binary_insertion_sort(my_list):

    for i in range(1, len(my_list)):
        v = my_list[i]
        j = binary_search(my_list, 0, i-1, v)
        my_list = my_list[:j] + [v] + my_list[j:i] + my_list[i+1:]
    return my_list

def main():
    numbers = [1, 3, 4, 6, 8, 13, 20, 22, 43, 55]
    index = binary_search(numbers, 0, len(numbers) - 1, 25451)
    print(index)


if __name__ == '__main__':
    main()
