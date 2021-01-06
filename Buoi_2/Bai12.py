"""
DÃY SỐ NGUYÊN TỐ:
    Nhập vào một số N, hiển thị các số nguyên tố từ 2 tới N?
"""

N = int(input('Nhập vào số tự nhiên N = '))
list_snt = []
for i in range(2, N+1):
    count = 0
    for j in range(2, i+1):
        snt = i%j
        if(snt == 0): count += 1
    if(count == 1): list_snt.append(i)
print('Danh sách các số nguyên tố từ 2 đến N là: ', list_snt)

