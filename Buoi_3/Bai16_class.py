"""
Xây dựng lớp Person:
    Gồm các Thuộc tính: họ tên (name), năm sinh (year), chiều cao height), cân nặng (weight)
    Gồm các Phương thức:
        Geeting(): Hiển thị thông tin của Person
        BMI(): Tính toán và xếp loại theo chỉ số BMI của Person
"""

class Person:
    def __init__(self, name = "Thủy", year = 1996, height = 1, weight = 50):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight
    
    def greeting(self):
        print("My name is", self.name)
        print("I'm", 2021 - self.year, "years old")
        print("Nice to meet you!")
    
    def bmi(self):
        return round(self.weight/(self.height**2), 2)
    
name = input('Your name: ')
year = int(input('Years of birthday: '))
height = float(input('Your height: '))
weight = float(input('Your weight: '))

p = Person(name, year, height, weight)
p.greeting()
print("BMI:", p.bmi())