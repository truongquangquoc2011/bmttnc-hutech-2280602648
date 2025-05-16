def dem_so_lan_xuat_hien(lst):
    count_dist ={}
    for item in lst:
        if item in count_dist:
            count_dist[item] +=1
        else:
            count_dist[item] =1
    return count_dist

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
wordList = input_string.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(wordList)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)