def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập danh sách từ người dùng và xử lý chuỗi 
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int,input_list.split(',')))

myTupple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("tuple: ",myTupple)