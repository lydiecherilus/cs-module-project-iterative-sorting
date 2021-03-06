def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1 
    while low <= high:
        middle = (low + high) // 2
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle
    return -1  # not found


letters = ['a', 'b', 'c', 'd']

print(linear_search(letters, 'a'))
print(linear_search(letters, 'd'))
print(linear_search(letters, 'e'))

print(binary_search(letters, 'a'))
print(binary_search(letters, 'd'))
print(binary_search(letters, 'e'))