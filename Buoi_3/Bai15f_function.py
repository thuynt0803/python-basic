"""
    DÃY SỐ NGUYÊN TỐ:
    Nhập vào một số N, hiển thị các số nguyên tố từ 2 tới N?
    
    YÊU CẦU: Viết hàm list_prime(): trả danh sách các số nguyên tố trong khoảng tử 1 đến n với tham số truyền vào là n
"""

def list_prime(n):
    list_snt = []
    if(n<2): print('N không phải là số nguyên tố!')
    else:
        for i in range(2, n+1):
            count = 0
            for j in range (2, i+1):
                du = i%j
                if(du == 0): 
                    count = count + 1
            if(count == 1): list_snt.append(i)

    return list_snt

n = int(input('Nhập số tự nhiên n = '))
print('Danh sách SNT trong khoảng từ 1 đến N là: ', list_prime(n))
