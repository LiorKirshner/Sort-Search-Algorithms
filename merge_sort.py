#merge: מיזוג
def merge_sort(A):
    if len(A) == 1:
        return A

    mid = len(A)//2
    left_list = merge_sort(A[:mid])
    right_list = merge_sort(A[mid:])
    return merge(left_list, right_list)


def merge(A,B):
    c=[]
    a=0
    b=0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            c.append(A[a])
            a=a+1
        else:
            c.append(B[b])
            b=b+1

    if a == len(A):
        while b<len(B):
            c.append(B[b])
            b += 1
    else:
        while a<len(A):
            c.append(A[a])
            a += 1
    return c



def merge_help(A, B):
    out = []
    a = 0
    b = 0
    while a<len(A) and b<len(B) :
        if A[a] < B[b] :
            out.append(A[a])
            a += 1
        else:
            out.append(B[b])
            b += 1

    while a<len(A):
        out.append(A[a])
        a +=1

    while b<len(B):
        out.append(B[b])
        b +=1

    return out



def merge3(a,b,c):
    out1 = merge_help(a,b)
    out2 = merge_help(out1, c)
    return out2




def main():
    test = [1,2,3,5,7,88,939]
    test2 = [5,6,8,99]
    test3 = [0,3,4,6,8888,9999]
    print(merge3(test, test2, test3))


if __name__ == '__main__':
        main()