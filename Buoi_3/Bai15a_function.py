"""
    Nhập vào tên và năm sinh của một người, tính tuổi của người đó và hiển thị ra màn hình thông báo.
    YÊU CẦU: Viết hàm greeting(): Trả về câu chào với tham số truyền vào là chuỗi họ tên và năm sinh
"""

import datetime

def greeting(hoten, namsinh):
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    tuoi = int((int(year) - namsinh))
    # print('Năm hiện tại: ', year)
    print('--- Hello world ---')
    print('Hi! My name is',hoten)
    print("I'm",tuoi, 'years old.')

hoten = input('Your name: ')
namsinh = input('Year of Birth: ')
greeting(hoten, int(namsinh))

