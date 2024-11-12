def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def hybrid_sort(arr, threshold=10):
    if len(arr) < threshold:
        return insertion_sort(arr)
    mid = len(arr) // 2
    left = hybrid_sort(arr[:mid], threshold)
    right = hybrid_sort(arr[mid:], threshold)
    return merge(left, right)

# Testing the Hybrid Sort
import random
arr = random.sample(range(1, 100), 20)  # Random array of 20 elements
print("Original Array:", arr)
sorted_arr = hybrid_sort(arr)
print("Sorted Array:", sorted_arr)

