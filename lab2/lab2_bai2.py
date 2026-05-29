import time

def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return memo[n]
        
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def fibonacci_iterative(n):
    """
    Sử dụng 2 biến để lưu F(n-1) và F(n-2), cập nhật qua mỗi vòng lặp.
    Độ phức tạp thời gian: O(n), không gian: O(1).
    """
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

if __name__ == "__main__":
    start = time.time()
    print("Naive F(30) =", fibonacci_naive(30))
    print(f"Thời gian Naive: {time.time() - start:.4f}s\n")

    start = time.time()
    print("Memo F(100) =", fibonacci_memo(100))
    print(f"Thời gian Memo: {time.time() - start:.6f}s")