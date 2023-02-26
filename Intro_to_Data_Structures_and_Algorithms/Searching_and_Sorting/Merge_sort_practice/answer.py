"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    elements = len(array)
    if (elements) < 2:
        return array

    current_position = 0
    for i in range(1, elements):
        if array[i] <= array[0]:
            current_position += 1
            temp = array[i]
            array[i] = array[current_position]
            array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position]
    array[current_position] = temp

    left = quicksort(array[0:current_position])
    right = quicksort(array[current_position+1:elements])

    array = left + [array[current_position]] + right
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]


print (quicksort(test))

# Memo
# [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# [4, 1, 3, 9, 20, 25, 6, 21, 14, 21]
# [4, 1, 3, 9, 25, 6, 21, 14, 20, 21]
# [4, 1, 3, 9, 6, 21, 14, 25, 20, 21]
# [4, 1, 3, 9, 6, 14, 21, 25, 20, 21]

# [4, 1, 3, 9, 6]
# [4, 1, 3, 6, 9]

# [4, 1, 3]
# [1, 3, 4]

# [1, 3, 4, 6, 9]


# [21, 25, 20, 21]
# [25, 20, 21, 21]
# [20, 21, 25, 21]


# [1, 3, 4, 6, 9, 20, 21, 21, 25]



