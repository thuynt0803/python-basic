"""
ĐỔI SỐ TỪ PHẬP PHÂN SANG NHỊ PHÂN:
    Nhập vào một số tự nhiên N (N>0), chuyển đổi số N sang hệ nhị phân.
"""

N = int(input('Số tự nhiên N = '))
n = N
list_nhiphan = [] 
while (n > 0):
    sd = str(n%2)
    list_nhiphan.append(sd)
    n = n//2
print('Hệ nhị phân của N là:',"".join(list_nhiphan[::-1]))  # Có thể thay dòng lệnh này bằng đoạn code bên dưới
"""
a =''
while (st!=[]):
  a = a + str (st.pop())
print('Số nhị phân là: ', a)
"""
