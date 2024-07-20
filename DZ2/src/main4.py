def check_palindrome(n: int) -> bool:
    if not(isinstance(n, int)):
        raise TypeError

    num = n
    item = 0
    is_palindr = 0

    while num != 0:
        item = num % 10
        is_palindr = is_palindr * 10 + item
        num = num // 10

    if is_palindr == n:
        return True

    return False







