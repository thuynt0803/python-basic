"""
KIỂM TRA N CÓ LÀ SỐ NGUYÊN TỐ?
    Nhập vào số tự nhiên N, cho biết N có phải là số nguyên tố hay không? (Số nguyên tố là số lớn hơn 1, chỉ chia hết cho 1 và chính nó)
"""


N = int(input('Số tự nhiên N = '))
if(N < 2): print('N không phải là số nguyên tố!')
else:
    count = 0
    for i in range(2, N+1):
        snt = N%i
        if(snt == 0): count += 1
    
    if(count == 1): print('N là số nguyên tố!')
    else: print('N không phải là số nguyên tố!') 
 