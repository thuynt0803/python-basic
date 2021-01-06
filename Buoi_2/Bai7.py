"""
    Nhập vào chiều cao (m) và cân nặng (kg) rồi tính chỉ số BMI của người đó theo công thức:
            BMI = Weight(Kg) / Height(m) ^2
    Dựa vào chỉ số BMI tính được đưa ra nhận xét về cơ thể của người đó theo các mức:
        . Underweight: BMI<18.5
        . NormalWeight: 18.5 <= BMI <= 24.9
        . Overweight: 25 <= BMI <=29.9
        . Obese: BMI>=30
"""

chieucao = float(input('Chiều cao (m):'))
cannang = float(input('Cân nặng (kg):'))

BMI = cannang/(chieucao**2)
if (BMI < 18.5): print('Underweight')
elif (18.5 <= BMI <= 24.9): print('Normalweight')
elif (25 <= BMI <= 29.9): print('Overweight')
else:
    print('Opese')
