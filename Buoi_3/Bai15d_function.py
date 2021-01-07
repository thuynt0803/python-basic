"""
    Nhập vào chiều cao (m) và cân nặng (kg) rồi tính chỉ số BMI của người đó theo công thức:
            BMI = Weight(Kg) / Height(m) ^2
    Dựa vào chỉ số BMI tính được đưa ra nhận xét về cơ thể của người đó theo các mức:
        . Underweight: BMI<18.5
        . NormalWeight: 18.5 <= BMI <= 24.9
        . Overweight: 25 <= BMI <=29.9
        . Obese: BMI>=30
        
    YÊU CẦU: Viết hàm bmi_show(): Trả về nhận xét dựa vào chỉ số BMI đã tính với 2 tham số truyền vào là chiều cao, cân nặng
"""
def bmi_show(height, weight):
    bmi = weight/(height**2)
    print('Chỉ số BMI: ',bmi, end= ' - ')
    if (bmi < 18.5): print('Underweight')
    elif (18.5 <= bmi <= 24.9): print('Normalweight')
    elif (25 <= bmi <= 29.9): print('Overweight')
    else:
        print('Opese')

height = float(input('Chiều cao (m): '))
weight = float(input('Cân nặng (kg): '))

bmi_show(height, weight)