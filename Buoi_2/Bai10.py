"""
Khởi tạo một danh sách bao gồm các phần tử là điểm của bạn (hệ 10). Hãy thực hiện:
    . Tạo một danh sách là các điểm chữ tương ứng với điểm hệ 10 ở trên.
    . Tính điểm trung bình Hệ 10 và Hệ 4
"""

diem10 = [9, 5, 3.6, 4.5, 8, 7, 7.6, 5.5, 8.5, 6, 9.4]
diemchu = []
diem4 = []
tong10 = 0
tong4 = 0
for i in diem10:
    if(9.0 <=i<=10):
        diemchu.append('A+')
        diem4.append(4.0)
    elif (8.5<=i<=8.9):
        diemchu.append('A')
        diem4.append(3.7)
    elif (8.0<=i<=8.4):
        diemchu.append('B+')
        diem4.append(3.5)
    elif (7.0<=i<=7.9):
        diemchu.append('B')
        diem4.append(3.0)
    elif (6.5<=i<=6.9):
        diemchu.append('C+')
        diem4.append(2.5)
    elif (5.5<=i<=6.4):
        diemchu.append('C')
        diem4.append(2.0)
    elif (5.0<=i<=5.4):
        diemchu.append('D+')
        diem4.append(1.5)
    elif (4.0<=i<=4.9):
        diemchu.append('D')
        diem4.append(1.0)
    elif (i<4.0):
        diemchu.append('F')
        diem4.append(0)
    tong10 = tong10 + i
for i in diem4:
    tong4 = tong4 + i
print('Danh sách điểm 10: ', diem10)
print('Danh sách điểm chữ: ', diemchu) 
print('Danh sách điểm 4: ', diem4)
print('-------------------------------------------------------------------------------------')
print('Tổng số sinh viên là: ', len(diem10))
print('ĐTB hệ 10: ', tong10/len(diem10))
print('ĐTB hệ 4: ', tong4/len(diem4))
