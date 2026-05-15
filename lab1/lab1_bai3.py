### Đoạn code ban đầu O(n^2)
def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
# Độ phức tạp: O(n^2)
# Có 2 vòng for lồng nhau
# Vòng ngoài chạy n lần
# Vòng trong không chạy toàn bộ n lần mà giảm dần
# khi i = 0 -> chạy n-1 lần
# khi i = 1 -> chạy n-2 lần ...
# Tổng số bước:
# (n-1) + (n-2) + ... + 1 = n(n-1)/2
# bỏ hằng số -> O(n^2)


### Phiên bản O(n)
def two_sum_linear(arr, target):
    seen = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return (seen[complement], i)
        seen[arr[i]] = i
    return None


### so sánh tốc độ xử lý
import time
arr = list(range(10000))
target = 16000

start = time.time()
print(two_sum_quadratic(arr, target))
time1 = time.time() - start
print(f"O(n^2) time: {time1:.4f}")

start = time.time()
print(two_sum_linear(arr, target))
time2 = time.time() - start
print(f"O(n) time: {time2:.4f}")