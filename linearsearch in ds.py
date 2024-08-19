def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


arr = [3, 5, 2, 8, 7]
target = 2
result = linear_search(arr, target)
print(f'Target found at index: {result}' if result != -1 else 'Target not found')
