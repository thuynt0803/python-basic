# ## 1. Hello world!
# print('Hello, world!')
# print('Hello', end= ' ')
# print('world')
# a = 1
# b = 2
# print('Gia tri a =', a, end=' va ')
# print('Gia tri b =', b)

# ## 2. Program to Add Two Numbers
# # Add 2 numbers
# num1 = 1.5
# num2 = 6.3 
# sum = num1 + num2
# print('Sum = ', sum)

# # Add 2 numbers with user input
# c = input('Enter first number: ')
# d = input('Enter second number: ')
# sum = c + d
# print('The sum of {0} and {1} is {2}'.format(c, d, sum))

# ## 3. Program to Find the Square Root
# # Chương trình Python để tính căn bậc hai
# num = 8
# cbh_num = num**0.5
# print('The square root of %0.3f is %0.3f'%(num ,cbh_num))  # the square root = căn bậc 2

#Sử dụng hàm 'cmath' để tính số phức
import cmath
sophuc = 1 + 2j
cbh_sophuc = cmath.sqrt(sophuc)
print('The square root of {0} is {1:0.3f} + {2:0.3f}j'.format(sophuc ,cbh_sophuc.real ,cbh_sophuc.imag))

