def counting_sort(A):

    maxi = max(A)
    size = int(maxi +1)
    B = [0] *size
    C = [0] * (len(A))

    # storing the count of each element - o(n)

    for i in A:      # for i in range(0, len(arr)) :
        B[i] += 1      # countArr[arr[i]] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array - o(size)
    for i in range(1, len(B)):
        B[i] += B[i-1]

    # Build the output character array - o(n)
    for i in range(len(A)-1, -1,-1):
        C[B[ A[i]] -1 ] = A[i]
        B[A[i]] -= 1

    return C


def main():
    A = [14,4,43,5546,3,9,5,2,0,5445]
    print("The list is: ", A)
    B = counting_sort(A)
    print("The sorted list is: ",  B)




if __name__ == '__main__':
    main()









