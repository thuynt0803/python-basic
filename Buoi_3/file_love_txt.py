"""
    Đọc dữ liệu từ file love.txt với nội dung ban đấu: 
        "Hà Nội lại đón một đợt không khí lạnh nữa rồi đấy cậu ... 

        Mùa lạnh, mùa của những tương tư, mùa của nỗi nhớ, mùa yêu, và mùa xa nhau! 
        
        Nhìn lại một năm qua .. cậu có những kỉ niệm nào đáng nhớ không?
        
        - Mình nghĩ là có đấy. Mình đã bỏ lỡ một vài thứ ...
        
        Dù sao, dẫu Hà Nội Lạnh, nhưng trong cậu ấm là được nhỉ!"
    
    Ghi đè:
    "Today is still a cold winter day, sit and look at the sky for a while and realize:

    Cold winter, being alone doesn't mean being alone. Feeling missing someone, but not picking up and making a call.

    Love, a little further away, no problem ... because when you love, you should try to get along better together, understand each other better, love is when you want to work a little bit, day by day, and feel better together ...

    However, I really miss someone ... "
"""

"""
# Ghi thêm dữ liệu vào file
import codecs
with codecs.open('./love.txt', 'a+', encoding= 'utf-8') as f:
    st = "\n\nStory 2:\n\n\tHà Nội lại đón một đợt không khí lạnh nữa rồi đấy cậu ... \n\n\tMùa lạnh, mùa của những tương tư, mùa của nỗi nhớ, mùa yêu, và mùa xa nhau! \n\n\tNhìn lại một năm qua .. cậu có những kỉ niệm nào đáng nhớ không? \n\n\t- Mình nghĩ là có đấy. Mình đã bỏ lỡ một vài thứ ... \n\n\tDù sao, dẫu Hà Nội Lạnh, nhưng trong cậu ấm là được nhỉ!"
    f.write(st)
    f.close() 
"""


import codecs
with codecs.open('./love.txt', encoding= 'utf-8') as f1:
    print(f1.read())  # Đọc toàn bộ nội dung của file sau khi được ghi thêm dữ liệu
    f1.close()
          
          
# st1 = f.read(50)       # Đọc 50 kí tự đầu tiên của file
# print(f.readline())    # Đọc từng dòng dữ liệu của file
# f = open('./love.txt', 'a+')  # Ghi tiếp dữ liệu vào file (sử dụng a+)
# f = open('./love.txt', 'w')  # Ghi đè dữ liệu vào file (sử dụng w)
"""
    st = "Story 1:\n\n\tToday is still a cold winter day, sit and look at the sky for a while and realize:\n\n\tCold winter, being alone doesn't mean being alone. Feeling missing someone, but not picking up and making a call.\n\n\tLove, a little further away, no problem ... because when you love, you should try to get along better together, understand each other better, love is when you want to work a little bit, day by day, and feel better together ...\n\n\tHowever, I really miss someone ..."
    f.write(st)
"""
