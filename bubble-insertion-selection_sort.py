def bubble_sort(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


def insertion_Sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i, len(A)):
            if A[j] < A[min_index]:
                A[j], A[min_index] = A[min_index], A[j]
    return A


def insertion_sort2(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A



def selection_sort_2list(A):
    B = []
    for i in range(len(A)):
        mini = min(A)
        B.append(mini)
        A.remove(mini)
    return B


def selection_sort(A):
    for i in range(0,len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[min_index], A[i] = A[i], A[min_index]
    return A


def selection_sort_rec(A, i=0):
    mini = i
    if i == (len(A)-1):
        return A
    for j in range(i+1, len(A)):
        if A[j] < A[mini]:
            mini = j
    A[mini], A[i] = A[i], A[mini]
    return selection_sort_rec(A, i+1)



    




def main():
    arr = [12, 11, 13, 5, 6]
    selection_sort_rec(arr)
    #arr2 = bubble_sort(arr)
   # arr3 = selection_sort_rec(arr)
    print(arr)

if __name__ == '__main__':
        main()