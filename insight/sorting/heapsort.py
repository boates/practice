

def parent(i):
    return (i-1) // 2 
    #return i // 2

def left(i):
    return 2*i + 1
    #return 2*i

def right(i):
    return left(i) + 1


def max_heapify(a, i, N):
    l = left(i)
    r = right(i)
    #N = len(a)
    if l < N and a[l] > a[i]:
        L = l
    else:
        L = i
    if r < N and a[r] > a[L]:
        L = r
    if L != i:
        a[i], a[L] = a[L], a[i]
        max_heapify(a, L, N)


def build_max_heap(a):
    N = len(a)
    for i in range(N//2-1, -1, -1):
        max_heapify(a, i, N)


def heapsort(a):
    build_max_heap(a)
    N = len(a)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        N = N - 1
        max_heapify(a, 0, N)


def main():

    print "Build Max Heap"
    a = [7, 10, 1, 7, -8, 0, 21, 1, 2, 8, 1, 6, 9, 7, -2]
    print a
    build_max_heap(a)
    print a

    print "Heap Sort"
    a = [7, 10, 1, 7, -8, 0, 21, 1, 2, 8, 1, 6, 9, 7, -2]
    heapsort(a)
    print a

if __name__ == "__main__":
    main()
