import heapq
import time
from lab4_bai1 import coin_change_greedy

def min_meeting_rooms(meetings):
    """
    Tìm số phòng họp tối thiểu.
    Tại sao dùng Heap? Để luôn theo dõi phòng nào kết thúc sớm nhất với chi phí O(log n).
    """
    if not meetings:
        return 0

    meetings.sort(key=lambda x: x[0])
    
    heap = []
    heapq.heappush(heap, meetings[0][1])
    
    for i in range(1, len(meetings)):
        start, end = meetings[i]
        
        if start >= heap[0]:
            heapq.heappop(heap)
            
        heapq.heappush(heap, end)
        
    return len(heap)

def coin_change_dp(amount, coins):
    """
    Coin Change dùng Dynamic Programming (Quy hoạch động).
    Luôn cho kết quả tối ưu toàn cục.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return -1 if dp[amount] == float('inf') else dp[amount]

def compare_coin_change(amount, coins):
    print(f"\n{'='*60}")
    print(f"So sánh Coin Change: amount={amount}, coins={coins}")
    
    start = time.time()
    greedy_res, greedy_detail = coin_change_greedy(amount, coins)
    greedy_time = time.time() - start
    print(f"[GREEDY] Kết quả: {greedy_res} xu, Thời gian: {greedy_time:.6f}s")
    
    start = time.time()
    dp_res = coin_change_dp(amount, coins)
    dp_time = time.time() - start
    print(f"[DP] Kết quả: {dp_res} xu, Thời gian: {dp_time:.6f}s")
    
    if greedy_res == dp_res:
        print("-> Greedy ĐÚNG, cho kết quả tối ưu và chạy nhanh hơn!")
    else:
        print(f"-> Greedy SAI, tốn nhiều hơn DP {greedy_res - dp_res} xu.")

if __name__ == "__main__":
    print(f"Số phòng họp tối thiểu: {min_meeting_rooms([(0, 30), (5, 10), (15, 20)])}")

    compare_coin_change(67, [25, 10, 5, 1])
    compare_coin_change(30, [25, 10, 1])