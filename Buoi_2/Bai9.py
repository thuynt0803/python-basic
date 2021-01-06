"""
    Nhập vào bảng cửu chương muốn in (1 – 10), hiển thị bảng cửu chương tương ứng với số vừa nhập. 
    (Lưu ý: Thực hiện kiểm tra giá trị nhập, chỉ thỏa mãn khi giá trị nhập vào trong khoảng [1,10]
"""

while True:
    x = int(input('Nhập vào bảng cửu chương muốn hiển thị [1-10]: '))
    if(1<=x<=10):
        break
    print('Nhập sai! Vui lòng nhập lại giá trị từ 1 đến 10.\n')

print('BẢNG CỬU CHƯƠNG', x)
for i in range(1,11):
    print('\t',x, 'x', i, '=', x*i)



