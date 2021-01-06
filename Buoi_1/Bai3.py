"""
BÀI 3: CHO BIẾT SỐ THỎ TRONG RỪNG
    Ban dầu trong rừng có một cặp thỏ, biết rằng cứ sau một tháng thì số lượng thỏ trong rừng tăng lên gấp đôi. 
    Hỏi sau x tháng thì trong rừng có bao nhiêu con thỏ? (Giả thiết các con thỏ không chết)
    Yêu cầu: Nhập vào số tháng x = 3
    Hiển thị thông báo kết quả: "Trong rừng có: 16 con thỏ"
"""
a = 2
print('Số thỏ trong rừng ban đầu:', a, 'con')
x = int(input('Số tháng: x = '))

# Số thỏ sau mỗi tháng
b = a**2 
# Tổng số thỏ sau x tháng
tong = b**2
print('Sau', x, 'tháng, trong rừng có:', tong, 'con thỏ')

