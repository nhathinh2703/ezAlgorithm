def SoNguyenTo(n):
    if n < 2: return False
    if n < 4: return True

    # Cách 1: Kiểm tra n%i == 0 với i từ 2 -> int(n**0.5)
    # Cách 2: Kiểm tra n%i == 0 với i từ 2 -> int(n/2)
    # Cách 3: Kiểm tra n%i == 0 với i từ 2 -> (n-1)

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True