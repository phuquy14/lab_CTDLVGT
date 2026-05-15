# Snippet 5 - Vòng for với range(i)
def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total
# Độ phức tạp: O(n^2)
# Giải thích:
# Vòng trong chạy i lần chứ không phải n lần cố đinh.
# Tổng số bước là:
# 0 + 1 + 2 + ... + (n-1) = n(n-1)/2
# Bỏ hằng số -> O(n^2)

# Snippet 6 - Vòng while + for
def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
        k = k * 2
    return total
# Độ phức tạp: O(n log n)
# Giải thích: 
# Vòng while nhân đôi k sau mỗi lần lặp nên chạy khoảng log2(n) lần.
# Mỗi lần while có vòng for chạy n lần.
# Tổng số bước: n * log(n)

# Snippet 7 - Duyệt list + toán tử in (list)
def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr:
            count += 1
    return count
# Độ phức tạp: O(n^2)
# Giải thích: 
# Vòng for chạy n lần.
# Toán tử "in" trên list có độ phức tạp O(n).
# Vì mỗi lần lặp đề tìm trong list nên tổng là n*n = O(n^2)

# Snippet 8 - Dùng set để tối ưu phép in
def snppet_8(arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count
# Độ phức tạp: O(n)
# Giải thích: 
# Tạo set từ list mất o(n)
# Vòng for chạy n lần
# Phép kiểm tra "x in s" với set có độ phức tạp trung bình O(1)
# Tổng cộng: O(n)
