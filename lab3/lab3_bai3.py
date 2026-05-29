import time

class Counter:
    def __init__(self):
        self.calls = 0
        self.pruned = 0
        
def subset_sum_basic(nums, target):
    """KHÔNG có pruning"""
    counter = Counter()
    result = []
    
    def backtrack(start, path, current_sum):
        counter.calls += 1

        if current_sum == target:
            result.append(path.copy())
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()
            
    backtrack(0, [], 0)
    return result, counter

def subset_sum_pruning(nums, target):
    """CÓ áp dụng 4 kỹ thuật pruning"""
    counter = Counter()
    result = []

    nums.sort() 

    total_remaining = sum(nums)
    
    def backtrack(start, path, current_sum, remaining_sum):
        counter.calls += 1
        
        if current_sum == target:
            result.append(path.copy())
            return

        if current_sum > target:
            counter.pruned += 1
            return

        if current_sum + remaining_sum < target:
            counter.pruned += 1
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
                
            if current_sum + nums[i] > target:
                counter.pruned += 1
                break
                
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i], remaining_sum - nums[i])
            path.pop()
            
    backtrack(0, [], 0, total_remaining)
    return result, counter

def compare_subset_sum(nums, target):
    print(f"\n--- So sánh Subset Sum (Target = {target}) ---")
    
    start = time.time()
    res1, c1 = subset_sum_basic(nums, target)
    time1 = time.time() - start
    
    start = time.time()
    res2, c2 = subset_sum_pruning(nums.copy(), target)
    time2 = time.time() - start
    
    print(f"Basic: Thời gian = {time1:.4f}s, Gọi hàm = {c1.calls}")
    print(f"Pruning: Thời gian = {time2:.4f}s, Gọi hàm = {c2.calls}, Cắt tỉa = {c2.pruned}")
    print(f"Tốc độ cải thiện: {time1/time2 if time2 > 0 else float('inf'):.2f}x")

if __name__ == "__main__":
    nums = list(range(1, 20))
    target = 50
    compare_subset_sum(nums, target)