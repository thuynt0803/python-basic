## Bài 6
"""
Nhập vào một ký tự chữ cái bất kỳ(không phân biệt chữ hoa-chữ thường), cho biết nó là nguyên âm hay phụ âm trong tiếng anh.
    5 chữ cái nguyên âm: U, E, O, A, I
    21 Chữ cái phụ âm: B, C, D, F, G, H, J K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z
"""

nguyenam = ['u', 'e', 'o', 'a', 'i']
print('Kiểm tra nguyên âm - phụ âm:')
x = input('Nhập vào x: ')
if(x.lower() in nguyenam): print('x là nguyên âm')
else: print('x là phụ âm') 

