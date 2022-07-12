def counting_sort(A, j):
    B = [0]*10
    C = [0]*(len(A)+1)

    for a in A:
        B[(a//(10**j)) % 10] += 1

    for i in range(1, len(B)):
        B[i] = B[i] + B[i - 1]

    for a in A[::-1]:
        digit = (a//(10**j)) % 10
        C[B[digit]] = a
        B[digit] -= 1

    return C[1:]


def radix_sort(A, digit_size):
    for i in range(digit_size):
        A = counting_sort(A, i)
    return A


def main():
    A = [331,233,457,657,839,436,322,345,720,355]
    print("original list: ", A)
    sorted_A = radix_sort(A, 4)
    print("sorted list: ", sorted_A)


if __name__ == '__main__':
    main()