"""
BÀI 2: TÍNH TUỔI
    Nhập vào tên và năm sinh của một người, tính tuổi của người đó và hiển thị ra màn hình thông báo.
    Yêu cầu:
        . Nhập vào họ tên: Nguyễn Thị Thu Thủy
        . Nhập vào năm sinh: 1999
    Hiển thị thông báo kết quả:
        Bạn "NGUYỄN THỊ THU THỦY" năm nay 21 tuổi!
"""
# Input
import datetime
now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
print('Năm hiện tại: ', year)

hoten = input('Họ tên: ')

namsinh = int(input('Năm sinh: '))
tuoi = int((int(year) - namsinh))

print('Bạn "', ten, '" năm nay', tuoi,'tuổi')