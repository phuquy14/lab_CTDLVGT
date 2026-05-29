def permutations(nums):
    """
    Tìm tất cả hoán vị của nums.
    Độ phức tạp: O(N! * N)
    """
    result = []
    def backtrack(path, remaining):
        if len(path) == len(nums):
            result.append(path.copy()) 
            return
            
        for i in range(len(remaining)):
            path.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path, new_remaining)
            path.pop()
            
    backtrack([], nums)
    return result

def combinations(nums, k):
    """
    Tìm tất cả tổ hợp k phần tử từ nums.
    Độ phức tạp: O(C(n,k) * k)
    """
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
    backtrack(0, [])
    return result

def subsets(nums):
    """
    Tìm tất cả tập con của nums.
    Độ phức tạp: O(2^n * n)
    """
    result = []
    def backtrack(start, path):
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
    backtrack(0, [])
    return result

def binary_strings(n):
    """
    Tìm tất cả chuỗi nhị phân độ dài n.
    Độ phức tạp: O(2^n * n)
    """
    result = []
    def backtrack(path):
        if len(path) == n:
            result.append("".join(path))
            return
            
        for choice in ['0', '1']:
            path.append(choice)
            backtrack(path)
            path.pop()
            
    backtrack([])
    return result

if __name__ == "__main__":
    print("=== Test Bài 1 ===")
    print(f"Permutations [1,2,3]: {len(permutations([1, 2, 3]))} kết quả")
    print(f"Combinations [1,2,3,4] chập 2: {len(combinations([1, 2, 3, 4], 2))} kết quả")
    print(f"Subsets [1,2,3]: {len(subsets([1, 2, 3]))} kết quả")
    print(f"Binary strings (n=3): {len(binary_strings(3))} kết quả")