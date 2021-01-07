"""
    Đọc dữ liệu trong file dayso1_bai17.txt:
        Tìm phần tử lớn nhất và nhỏ nhất trong dãy, sau đó thực hiện đổi chỗ phần tử lớn nhất xuất hiện đầu tiên trong dãy cho phần tử nhỏ nhất xuất hiện đầu tiên trong dãy.
        Lưu dãy mới đã đổi chỗ sang file dayso2_bai17.txt
"""

import codecs
with codecs.open('./demo_fileB17.txt, encoding='utf-8') as f:
    st = f.read()  # Đọc file
    f.close() 
    print('Nội dung của file: ')
    print(st)

