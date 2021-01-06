"""
BÀI 5: Thống kê điểm Học viên
    Khởi tạo một danh sách gồm các điểm thi môn “Python for Analysis and machine learning” 
    của lớp AIV_Japan01 (Điểm chữ: A, B, C, D, F). Yêu cầu:
        1) Cho biết số sinh viên trong lớp
        2) Có bao nhiêu sinh viên phải học lại môn này (điểm F).
        3) Có bao nhiêu sinh viên có điểm từ B trở lên.
        4) Sinh viên đầu tiên và cuối cùng trong lớp đã nghỉ học, tạo một bảng điểm mới 
           và loại bỏ điểm của các sinh viên này ra khỏi danh sách điểm.
"""

diem_AIV_Japan01 = ['C','B','A','B','B','A','C','A','A','A','F','D','A','A','C','A','B','A','D','A','F','A','A','C','F']
print('Danh sách gồm các điểm thi môn “Python for Analysis and machine learning” của lớp AIV_Japan01:', diem_AIV_Japan01)
print('----------- THỐNG KÊ ---------------')
# Yêu cầu 1
print('1. Số sinh viên trong lớp là:', len(diem_AIV_Japan01))

# Yêu cầu 2
print('2. Số sinh viên phải học lại:', diem_AIV_Japan01.count('F'))

# Yêu cầu 3
x = diem_AIV_Japan01.count('A')
y =diem_AIV_Japan01.count('B')
z = x + y
print('3. Số sinh viên có điểm từ B trở lên:', z)

# Yêu cầu 4
diem_AIV_Japan01.pop()  # Xóa vị trí cuối ds
diem_AIV_Japan01.pop(0) # Xóa vị trí đầu ds
print('4. Bảng điếm sau khi đã loại bỏ sinh viên đầu tiên và cuối cùng nghỉ học là: ', diem_AIV_Japan01)
