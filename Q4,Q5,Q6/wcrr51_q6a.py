def hybrid_sort(a):
    if len(a) < 5:
        return selection_sort(a.copy())

    middle = len(a) // 2
    left = a[0:middle]
    right = a[middle:len(a)]

    leftsorted = hybrid_sort(left)
    rightsorted = hybrid_sort(right)
    
    return merge(leftsorted, rightsorted)


def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.extend(left)
            left = []
        else:
            result.extend(right)
            right = []

    return result


def selection_sort(a):
    for i in range(len(a) - 1):
        elem = a[i]
        pos = i
        for j in range(i + 1, len(a)):
            if a[j] > elem:
                elem = a[j]
                pos = j
        a[i], a[pos] = a[pos], a[i]
    return a


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            return False
    return True

if __name__ == '__main__':
    print(hybrid_sort([5, 6, 4, 7, 3, 8, 2, 9, 1, 0]))
