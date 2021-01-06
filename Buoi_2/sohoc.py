""" Toán tử số học, so sánh, logic trong Python """

a = 5
b = 4
print('a =', a)
print('b =', b)
# Các toán tử số học trong python
print('\n=== Các toán tử số học ===')
print('Tổng a + b =', a + b)
print('Hiệu a - b =', a - b)
print('Tích a * b =', a * b)
print('Thương a / b =', a / b)
print('Thương nguyên a // b =', a // b)
print('Thương dư a % b =', a % b)
print('Mũ a ** b =', a ** b)


# Các toán tử so sánh trong python
kt = a>b
print('\n=== Các toán tử so sánh ===')
print(type(kt))
print('1) SS lớn hơn (a>b):', a>b)
print('2) SS nhỏ hơn (a<b):', a<b)
print('3) SS bằng    (a=b):', a==b)
print('4) SS lớn hơn hoặc bằng (a>=b):', a>=b)
print('5) SS nhỏ hơn hoặc bằng (a<=b):', a<=b)
print('6) SS khác   (a!=b):', a!=b)

# Các toán tử logic trong python
x = 15
y = True

kt = (x>3) and (x<10) #hoặc kt = (x>3) & (x<10)
kt2 = (x>3) or (x<10) #hoặc kt = (x>3) | (x<10)
kt3 = not y
print('\n=== Các toán tử logic ===')
print ('1) Phép toán AND:', kt)
print ('2) Phép toán OR :', kt2)
print ('3) Phép toán NOT:', kt3)
