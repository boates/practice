

def merge(a, b):
    s = []
    while a and b:
        if a[0] < b[0]:
            s.append(a.pop(0))
        else:
            s.append(b.pop(0))
    return s + a + b


def mergesort(a):
    l = len(a)//2
    if l == 0:
        return a
    x = mergesort(a[:l])
    y = mergesort(a[l:])
    return merge(x, y)


def mergesort_iterative(a):

    if len(a) == 1: return a
    s = [[i] for i in a]

    while len(s) > 1:
        i = 0
        n = []
        while i < len(s):
            if i + 1 == len(s):
                n.append(s[i])
            else:
                n.append(merge(s[i], s[i+1]))
            i += 2
        s = n
    return s[0]


def main():
    
    #print merge( [4, 6, 8], [3, 5, 7])

    a = [34, 5, 2, 56, -45, 6, 6, 2, 12, 0, 5]
    print a
    print mergesort(a)
    print mergesort_iterative(a)


if __name__ == "__main__":
    main()
