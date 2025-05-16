so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44 # giờ làm tiêu chuẩn mỗi tuần 
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5 # biến lính tỗng thu nhập
print("Số tiền thực lĩnh của bạn là: {}".format( thuc_linh)) # phương thức format này sẽ đưa giá trị của biến thuc_linh đó vào placeholder 