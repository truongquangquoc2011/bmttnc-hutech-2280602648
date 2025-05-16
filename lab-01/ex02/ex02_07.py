#Nhap cac dong van ban tu nguoi dung
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    # append() dùng để thêm các dòng văn bản vào  lines []
# chuyển các dòng văn bản thành chữ hoa và in ra 
print("\nCác dòng văn bản đã nhập sau khi chuyển thành chữ hoa là: ")
for line in lines:
    print(line.upper())