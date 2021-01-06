"""
BÀI 1: CHIA KẸO CHO HỌC SINH LỚP 1
    Cô có n cái kẹo, có m học sinh trong lớp. Hãy giúp cô chia đều số kẹo cho tất cả học sinh.
    Yêu cầu:
        . Nhập vào số kẹo của cô (n)
        . Nhập vào số học sinh trong lớp (m)
    Cho biết: 
        . Mỗi học sinh được nhận bao nhiêu cái kẹo?
        . Cô còn lại bao nhiêu cái kẹo?
"""

# Input
n = int(input('Số kẹo của cô: n = '))
m = int(input('Số học sinh trong lớp: m = '))

# Output
print('Số kẹo mỗi học sinh được nhận là: ', n//m)
print('Số kẹo còn lại của cô là: ', n%m)
