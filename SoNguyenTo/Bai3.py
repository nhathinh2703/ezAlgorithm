# Tìm số nguyên tố lớn nhất nhỏ hơn n.
# Cách 1: Duyệt từ 2 đến (n-1) để tìm số nguyên tố gần n nhất.
def SoNguyenTo(n):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Bước 1: Nhập n từ bàn phím
n = int(input("Nhập n: "))
# Bước 2: Khởi tạo biến ds là danh sách rỗng
ds = []
# Bước 3: Duyệt i từ 2 đến (n-1):
#              Nếu i là số nguyên tố thì thêm i vào ds
for i in range(2, n):
        if SoNguyenTo(i):
            ds.append(i)
# Bước 4: Nếu độ dài của ds > 0:
#               In phần tử cuối cùng của ds
#         Ngược lại:
#               In -1
if len(ds) > 0:
    print(ds[len(ds) - 1])
else:
    print(-1)

# Cách 2: Duyệt ngược từ (n-1) về 2 để tìm số nguyên tố gần n nhất.

# Bước 1: Khởi tạo i = n-1 và soCanTim = -1
# Bước 2: Trong khi i >= 2:
#              Nếu i là số nguyên tố thì:
#                   gán soCanTim = i
#                   thoát khỏi vòng lặp
#              Giảm i đi 1
# Bước 3: In soCanTim
