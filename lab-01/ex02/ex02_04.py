#tạo mảng rỗng 
j=[]
# duyệt qua các số từ 2000 tới 3200 , kiểm tra số i có chia hết cho 7 và không phải là bội số của 5 không
for i in range(2000,3200):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(',' .join(j))