import random


def partition_2list(A,k):
    left = 0
    right = len(A)-1
    B = [0]*len(A)
    for i in range(len(A)):
        if A[i] > k:
            B[right] = A[i]
            right = right-1
        else:
            B[left] = A[i]
            left = left+1
    return B


def partitionn(array, left, right):
    pivot = array[left]
    mini = left

    for i in range(left, right+1):
        if array[i] < pivot:
            mini +=1
            array[i], array[mini] = array[mini] , array[i]
            print(array)
    array[mini] , array[left] = array[left], array[mini]
    print(mini)
    print(array)

    return mini


def quick(array, left, right):
    if left < right:
        pi = partitionn(array,left,right)

        quick(array, left, pi-1)
        quick(array,pi+1,right)











def partition(array, left, right):
    leftwall = left
    pivot = array[left]

    for i in range(left, right+1):
        if array[i] < pivot:
            leftwall += 1
            array[i], array[leftwall] = array[leftwall], array[i]

    (array[leftwall], array[left]) = (array[left], array[leftwall])
    return leftwall


def quick_sort(array, left, right):
    if left < right:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, left, right)

        # Recursive call on the left of pivot
        quick_sort(array, left, pi-1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, right)


def randomize_quick_sort(a,left,right):
    if left < right:
        pivot = randomize_partition(a, left, right)
        randomize_quick_sort(a, left, pivot - 1)
        randomize_quick_sort(a, pivot+1, right)



def randomize_partition(a, left, right):
    rand_pivot = random.randint(left, right)
    a[rand_pivot], a[left] = a[left], a[rand_pivot]
    last_min = partition(a, left, right)
    return last_min






def main():
    A = [5, 8, 1, 9, 14, 3, 56, 782, 2, 51, 11, 7]
    print("The list is: ", A)
    quick(A, 0, len(A) - 1)
    print("The sorted list is: ", A)


if __name__ == '__main__':
    main()