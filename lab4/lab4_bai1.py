def activity_selection(activities):
    """
    Hàm 1: Chọn số lượng hoạt động tối đa không chồng lấp.
    Chiến lược Greedy: Chọn hoạt động kết thúc sớm nhất để dư dả thời gian cho hoạt động sau.
    """
    if not activities:
        return []
        
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish = activities[0][1]

    for i in range(1, len(activities)):
        start, finish = activities[i]
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
            
    return selected

def coin_change_greedy(amount, coins):
    """
    Hàm 2: Đổi tiền bằng số xu ít nhất (Greedy).
    Chiến lược Greedy: Chọn xu mệnh giá lớn nhất có thể trước.
    """
    coins.sort(reverse=True)
    count = 0
    result = []
    
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
            count += 1
            
    if amount == 0:
        return count, result
    return -1, []

def fractional_knapsack(capacity, items):
    """
    Hàm 3: Bài toán Ba lô phân số (Fractional Knapsack).
    Chiến lược Greedy: Chọn vật có tỷ lệ Giá trị / Trọng lượng (ratio) cao nhất.
    """
    items_with_ratio = []
    for weight, value in items:
        ratio = value / weight
        items_with_ratio.append((weight, value, ratio))

    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    result = []
    
    for weight, value, ratio in items_with_ratio:
        if remaining_capacity == 0:
            break
            
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
            result.append((weight, value, 1.0))
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            result.append((weight, value, fraction))
            remaining_capacity = 0
            
    return total_value, result

def min_intervals_remove(intervals):
    """
    Hàm 4: Tìm số khoảng ít nhất cần xóa để không chồng lấp.
    Chiến lược: Số khoảng cần xóa = Tổng số khoảng - Số khoảng tối đa có thể giữ lại.
    """
    if not intervals:
        return 0
    max_keep = activity_selection(intervals)
    return len(intervals) - len(max_keep)

if __name__ == "__main__":
    print("Test Activity Selection:", activity_selection([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9)]))
    print("Test Coin Change (Hệ lạ):", coin_change_greedy(30, [25, 10, 1]))
    print("Test Fractional Knapsack:", fractional_knapsack(50, [(10, 60), (20, 100), (30, 120)]))
    print("Test Min Intervals Remove:", min_intervals_remove([(1, 2), (2, 3), (3, 4), (1, 3)]))