def heapify(A, i, heap_size):
    left = 2*i + 1  # left index
    right = 2*i + 2  # right index
    maxi = i  # initialize

    # מוצאים איבר מקסימלי מבין האבא ו2 הבנים שלו
    if left < heap_size and A[maxi] > A[left]:  # if father < left
        maxi = left
    if right < heap_size and A[maxi] > A[right]:  # if ans < right
        maxi = right

    # אם יש צורך בהחלפה
    if maxi != i:  # if we need to swap
        A[i], A[maxi] = A[maxi], A[i]
        heapify(A, maxi, heap_size)


#בניית ערמה
def build_heap(A):
    for i in range(len(A)//2, -1, -1):
        heapify(A, i, len(A))


def heap_sort(A):
    build_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)


def main():
    A = [5,13,2,25,7,17,20,8,4]
    heap_sort(A)
    print(A)


if __name__ == '__main__':
    main()