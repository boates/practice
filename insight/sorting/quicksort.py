

def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        print "---------------"
        print p, r, q 
        print a
        quicksort(a, p, q-1)  # q = 3
        quicksort(a, q+1, r)


def partition(a, p, r):
    """
    length = 6
    0 1 2 3 4 5
    p         r
    """
    print a[p:r+1]
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1    

def main():
    
    a = [5, 3, 7, -12, 8, 4, 5, 4, -12, 6]

    print "Original: ", a
    quicksort(a, 0, len(a)-1)
    print a

if __name__ == "__main__":
    main()


