"""
    Ban dầu trong rừng có một cặp thỏ, biết rằng cứ sau một tháng thì số lượng thỏ trong rừng tăng lên gấp đôi. 
    Hỏi sau x tháng thì trong rừng có bao nhiêu con thỏ? (Giả thiết các con thỏ không chết)
    YÊU CẦU: Viết hàm rabbit_count(): tính số thỏ trong rừng khi truyền vào số tháng.

    Gợi ý:
        sau 1 tháng: 2*2 = 2^(1+1) con
        sau 2 tháng: 2*2*2 = 2^(2+1) con
        sau 3 tháng: 2*2*2*2 = 2^(3+1) con
        sau n tháng = 2^(n+1) con


"""

def rabbit_count(NumberOfMonths):
    total = 2**(NumberOfMonths +1)
    return total

NumberOfMonths = int(input('Number of months: '))
print('Total number of rabbits in the forest after the given number of months:', rabbit_count(NumberOfMonths))

