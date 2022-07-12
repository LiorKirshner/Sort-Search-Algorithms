#מיון הכנסה
def insertion_Sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i, len(A)):
            if A[j] < A[min_index]:
                A[j], A[min_index] = A[min_index], A[j]
    return A



def bucket_sort(A):
    B = [ [] for i in A ]
    C = []

    # inside the array elements in the right buckets
    for i in A:
        B[(int(i * len(A)))].append(i)

    # sort the inner list with side code
    for i in B:
        insertion_Sort(i)

    # C - sorted list
    for i in B:
        for j in i:
            C.append(j)

    return C


def main():

    x = [0.897, 0.565, 0.656,
         0.1234, 0.665, 0.3434,
         0.2, 0.2221,0.0002]
    print(x)
    print("Sorted Array is")
    print(bucket_sort(x))


if __name__ == '__main__':
        main()
