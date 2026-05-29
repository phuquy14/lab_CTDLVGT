import time

class Counter:
    def __init__(self):
        self.total_calls = 0
        self.solutions = 0
    def report(self):
        print(f"Tổng số lần gọi đệ quy: {self.total_calls}")
        print(f"Số giải pháp: {self.solutions}")

def is_safe(board, row, col, n):
    """Kiểm tra đặt quân hậu ở (row, col) có bị ăn không"""
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def is_board_valid_entirely(board):
    """Hàm phụ dùng cho phần B (Không Pruning) để check lại toàn bộ board"""
    for r1 in range(len(board)):
        for r2 in range(r1 + 1, len(board)):
            c1, c2 = board[r1], board[r2]
            if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                return False
    return True

def print_board(solution, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_n_queens_no_pruning(n):
    """Phần B: N-Queens KHÔNG Pruning (Duyệt cạn rồi mới check)"""
    counter = Counter()
    result = []
    board = []
    
    def backtrack(row):
        counter.total_calls += 1
        if row == n:
            if is_board_valid_entirely(board):
                result.append(board.copy())
                counter.solutions += 1
            return
            
        for col in range(n):
            board.append(col)
            backtrack(row + 1)
            board.pop()
            
    backtrack(0)
    counter.report()
    return result

def solve_n_queens_with_pruning(n):
    """Phần C: N-Queens CÓ Pruning (Kiểm tra trước khi đi sâu)"""
    counter = Counter()
    result = []
    board = []
    
    def backtrack(row):
        counter.total_calls += 1
        if row == n:
            result.append(board.copy())
            counter.solutions += 1
            return
            
        for col in range(n):
            if is_safe(board, row, col, n):
                board.append(col)
                backtrack(row + 1)
                board.pop()
                
    backtrack(0)
    counter.report()
    return result

def compare_n_queens(n):
    """Phần D: So sánh hiệu suất"""
    print(f"\n{'='*50}")
    print(f"So sánh N-Queens với N = {n}")
    print(f"{'='*50}")
    
    print("\n[1] KHÔNG có pruning:")
    start = time.time()
    res1 = solve_n_queens_no_pruning(n)
    time1 = time.time() - start
    print(f"Thời gian: {time1:.6f}s")
    
    print("\n[2] CÓ pruning:")
    start = time.time()
    res2 = solve_n_queens_with_pruning(n)
    time2 = time.time() - start
    print(f"Thời gian: {time2:.6f}s")
    
    print(f"\nTốc độ tăng: {time1/time2 if time2 > 0 else float('inf'):.2f}x")
    if res2:
        print(f"\nMột giải pháp mẫu cho {n}-Queens:")
        print_board(res2[0], n)

if __name__ == "__main__":
    compare_n_queens(4)
    compare_n_queens(6)