"""Sorting algorithms: Merge Sort and Quick Sort."""


def merge_sort(arr):
    """Recursively sorts a list using Merge Sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    """Helper function to merge two sorted lists."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr):
    """Sorts a list using Quick Sort (recursive, functional style)."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", nums)
    print("Sorted with Merge Sort:", merge_sort(nums))
    print("Sorted with Quick Sort:", quick_sort(nums))
