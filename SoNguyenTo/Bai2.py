def SoNguyenTo(n):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Đếm số lượng số nguyên tố trong đoạn [a, b]