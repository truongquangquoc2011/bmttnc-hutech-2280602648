def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Nhập danh sách từ người dùng và xử lý chuỗi 
inputList = input("Nhập danh sách các số , cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputList.split(',')))
# sử dụng hàm và in kết quả
tongChan = tinh_tong_so_chan(numbers)
print("Tổng số chẳn trong list là ", tongChan)