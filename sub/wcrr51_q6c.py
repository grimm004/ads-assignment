def hybrid_sort(a):
    # If the number of items in a is 4 or less
    if len(a) < 5:
        # Return the selection sort of a copy of a
        return selection_sort(a.copy())

    # If the number of items in a greater than 4,
    # calculate the middle value
    middle = len(a) // 2
    # Create a list for the items left of the middle in the list to sort
    left = a[0:middle]
    # Create a list of the items right of the middle in the list to sort
    right = a[middle:len(a)]

    # Sort the left side with a hybrid sort
    leftsorted = hybrid_sort(left)
    # Sort the right side with a hybrid sort
    rightsorted = hybrid_sort(right)

    # Merge the two sorted lists together and return it
    return merge(leftsorted, rightsorted)


def merge(left, right):
    # Define a list to sort the resultant items
    result = []

    # While there are items in the left sorted list or the right sorted list
    while len(left) > 0 or len(right) > 0:
        # If there are items in both lists
        if len(left) > 0 and len(right) > 0:
            # If the first item in the left list is greater than the first item in the right list
            if left[0] > right[0]:
                # Append the first item of the left list to the result
                result.append(left[0])
                # Remove the first item from the left list
                left = left[1:]
            else:
                # If the above condition is not met, add the first item in the right list to the result
                result.append(right[0])
                # Remove the first item from the right list
                right = right[1:]
        # Else if there are still items in the left list
        elif len(left) > 0:
            # Add the rest of the left list to the right list
            result.extend(left)
            # Clear the left list
            left = []
        else:
            # Else add the reft of the right list to the results list
            result.extend(right)
            # Clear the right list
            right = []

    # Return the merged list
    return result


def selection_sort(a):
    # Loop through each item in the list bar the last one
    for i in range(len(a) - 1):
        # Access the current element being referenced
        elem = a[i]
        # Sore the position of the current element
        pos = i
        # Loop through each item beyond the current one in the list
        for j in range(i + 1, len(a)):
            # If the current inner item is larager than the current item
            if a[j] > elem:
                # Select the current inner item for swapping
                elem = a[j]
                # Sore the swap location in pos
                pos = j
        # Swap the two items
        a[i], a[pos] = a[pos], a[i]
    # Return the sorted list
    return a


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            return False
    return True

if __name__ == '__main__':
    print(hybrid_sort([5, 6, 4, 7, 3, 8, 2, 9, 1, 0]))
    #from random import randint
    #while True:
        #a = [randint(0, 1000) for i in range(randint(100, 10000))]
        #b = hybrid_sort(a)
        #print(b)
        #print(len(a), len(b), len(a) == len(b), is_sorted(b))
