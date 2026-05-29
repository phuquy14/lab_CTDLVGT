import time
import random

def find_content_children(g, s):
    """
    Tìm số trẻ tối đa được phát bánh.
    g: list độ tham lam của trẻ
    s: list kích thước bánh
    """
    g.sort()
    s.sort()
    
    child_i = 0
    cookie_j = 0
    
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
        
    return child_i

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_bikes(workers, bikes):
    """
    Ghép worker với bike sao cho tổng khoảng cách ngắn nhất.
    """
    distances = []
    for w_idx, worker in enumerate(workers):
        for b_idx, bike in enumerate(bikes):
            dist = manhattan_distance(worker, bike)
            distances.append((dist, w_idx, b_idx))
            
    distances.sort(key=lambda x: (x[0], x[1], x[2]))
    
    assigned_workers = set()
    assigned_bikes = set()
    result = [-1] * len(workers)
    
    for dist, w_idx, b_idx in distances:
        if w_idx not in assigned_workers and b_idx not in assigned_bikes:
            assigned_workers.add(w_idx)
            assigned_bikes.add(b_idx)
            result[w_idx] = b_idx
            
    return result

def generate_test_data(n):
    activities = []
    for i in range(n):
        start = random.randint(0, 100)
        duration = random.randint(1, 20)
        activities.append((start, start + duration))
    return activities

def benchmark_activity_selection(sizes):
    print("\n--- Benchmark Activity Selection ---")
    from lab4_bai1 import activity_selection
    
    for size in sizes:
        activities = generate_test_data(size)
        start = time.time()
        activity_selection(activities)
        elapsed = time.time() - start
        print(f"Size = {size:<6} | Thời gian: {elapsed:.6f}s")

if __name__ == "__main__":
    print("Test Cookies:", find_content_children([1, 2, 3], [1, 1]))
    
    workers = [(0,0), (2,1)]
    bikes = [(1,2), (3,3)]
    print("Test Bikes:", assign_bikes(workers, bikes))
    
    sizes = [100, 500, 1000, 5000, 10000]
    benchmark_activity_selection(sizes)