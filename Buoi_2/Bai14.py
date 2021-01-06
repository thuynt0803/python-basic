"""
TÌM SỐ MAX - MIN - MEAN
    Khởi tạo một dãy số là chiều cao của sinh viên trong một lớp (m). Thực hiện:
        . Hiển thị chiều cao của sinh viên cao nhất – thấp nhất trong lớp
        . Tính chiều cao trung bình của sinh viên trong lớp.
        . Số lượng sinh viên trong lớp có chiều cao lớn hơn hoặc bằng chiều cao trung bình của lớp
"""

n = [1.50, 1.60, 1.45, 1.50, 1.65, 1.70, 1.57, 1.59, 1.63, 1.72, 1.75]  #Danh sách chiều cao của sinh viên trong lớp
print('Tổng số sinh viên trong lớp:', len(n))
print('SV có chiều cao cao nhất lớp:', max(n), 'm')
print('SV có chiều cao thấp nhất lớp:', min(n), 'm')
# Tính chiều cao TB
tong = 0
for i in n:
    tong = tong + i
print('Chiều cao trung bình của sinh viên trong lớp là:', tong/len(n))
# Số sinh viên có chiều cao >= chiều cao TB
dem = 0
for i in n:
    if(i >= (tong/len(n))):
        dem += 1
print('Số sinh viên trong lớp có chiều cao >= chiều cao TB là: ', dem)







