import time
import random

def merge(left, right):
    """Trộn 2 mảng đã sắp xếp thành 1 mảng sắp xếp"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    """Sắp xếp mảng bằng Merge Sort, độ phức tạp O(n log n)"""
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

def quick_sort(arr):
    """Sắp xếp mảng bằng Quick Sort, độ phức tạp trung bình O(n log n)"""
    if len(arr) <= 1:
        return arr
        
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr_small = [random.randint(1, 1000) for _ in range(100)]
    arr_large = [random.randint(1, 10000) for _ in range(5000)]

    start = time.time()
    sorted_small = merge_sort(arr_small.copy())
    print(f"Merge Sort 100 phần tử: {time.time() - start:.6f}s")

    start = time.time()
    sorted_large = quick_sort(arr_large.copy()) 
    print(f"Quick Sort 5000 phần tử: {time.time() - start:.6f}s")

    start = time.time()
    sorted_builtin = sorted(arr_large.copy())
    print(f"Python sorted() 5000 phần tử: {time.time() - start:.6f}s")