"""
    Đọc dữ liệu trong file dayso1_bai17.txt
    Yêu cầu:
        Tìm phần tử lớn nhất và nhỏ nhất trong dãy, sau đó thực hiện đổi chỗ phần tử lớn nhất xuất hiện đầu tiên trong dãy cho phần tử nhỏ nhất xuất hiện đầu tiên trong dãy.
        Lưu dãy mới đã đổi chỗ sang file dayso2_bai17.txt
    
"""

# Đọc file
f = open('./dayso1_bai17.txt')
st = f.read()
f.close()
print(st)

# Tách chuỗi, đưa về danh sách phần tử
list_st = st.split()  # dùng split() để tách chuỗi thành list phần tử cách nhau bởi dấu cách
print(list_st)

# Ép kiểu về danh sách số tự nhiên
list_so = []
for i in list_st:
    list_so.append(int(i))
print(list_so)

# Tim max, min
max_ds = max(list_so)
min_ds = min(list_so)
print('Max =', max_ds)
print('Min =', min_ds)

# Tìm vị trí max, min đầu tiên
index_max = index_min = 0
for i in range(0, len(list_so)):
    if list_so[i] == max_ds:
        index_max = i
        break
for i in range(0, len(list_so)):
    if list_so[i] == min_ds:
        index_min = i
        break
print('Vị trí max: ', index_max)
print('Vị trí min: ', index_min)

# Đổi chỗ max <-> min
list_so[index_max] = min_ds
list_so[index_min] = max_ds
print('Danh sách sau khi đổi chỗ max-min đầu tiên:', list_so)

# Chuyển lại danh sách về chuỗi
st = ''
for i in list_so:
    st = st + str(i) + " "
print(st)

# Ghi đè danh sách vào file mới
f = open('dayso2_bai17.txt', 'w')
f.write(st)
f.close()

