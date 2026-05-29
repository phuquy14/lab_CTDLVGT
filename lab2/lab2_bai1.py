def sum_to_n(n):
    """
    Hàm 1: Tính tổng từ 1 đến n
    - Base case: Nếu n = 0 thì trả về 0, n = 1 thì trả về 1.
    - Recursive case: Tổng từ 1 đến n = n + tổng từ 1 đến (n-1).
    - Độ phức tạp Big-O: O(n) do hàm gọi đệ quy n lần.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)


def power(n, k):
    """
    Hàm 2: Tính n mũ k
    - Base case: Nếu số mũ k = 0 thì trả về 1. Nếu cơ số n = 0 thì trả về 0.
    - Recursive case: n^k = n * n^(k-1).
    - Độ phức tạp Big-O: O(k) do hàm gọi đệ quy k lần.
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    return n * power(n, k - 1)


def reverse_string(s):
    """
    Hàm 3: Đảo ngược chuỗi
    - Base case: Nếu chiều dài chuỗi <= 1 (rỗng hoặc 1 ký tự), trả về chính chuỗi đó.
    - Recursive case: Đảo phần còn lại của chuỗi + ký tự đầu tiên.
    - Độ phức tạp Big-O: O(n) với n là chiều dài chuỗi.
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    """
    Hàm 4: Kiểm tra chuỗi Palindrome (đọc xuôi ngược như nhau)
    - Base case: Chuỗi rỗng hoặc 1 ký tự luôn là Palindrome -> True.
    - Recursive case: Nếu ký tự đầu và cuối khác nhau -> False. 
                      Nếu giống nhau, kiểm tra đệ quy phần giữa chuỗi.
    - Độ phức tạp Big-O: O(n) vì có tối đa n/2 lần so sánh.
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

if __name__ == "__main__":
    print("Test Hàm 1:", sum_to_n(10))
    print("Test Hàm 2:", power(2, 5))
    print("Test Hàm 3:", reverse_string("python"))
    print("Test Hàm 4:", is_palindrome("madam"))