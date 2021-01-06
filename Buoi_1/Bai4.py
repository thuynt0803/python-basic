"""
BÀI 4: CHUỖI VĂN BẢN
    "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 - 1969)"
    Yêu cầu:
        . Cho biết số ký tự có trong đoạn văn trên?
        . Cho biết trong đoạn có chứa từ nào sau đây không? (không phân biệt chữ hoa, chữ thường):
            - "hồ chí minh"
            - "non sông"
        . Tách đoạn văn thành các câu bởi dấu chấm (.)
        . Cho biết trong đoạn văn trên có ký tự nào khác ký tự chữ và số hay không?
        . Thay thế các từ `Việt Nam` bằng `VIỆT NAM` trong đoạn văn trên
"""
vanban = 'Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 - 1969)'
a = 'hồ chí minh'
x = a.upper() in vanban
y = 'non sông' in vanban
print(vanban)

# Đếm số ký tự trong đoạn văn
print('\n- Số ký tự trong đoạn văn trên là: ', len(vanban))

# Trả về True nếu có trong chuỗi
# Trả về false nếu không có trong chuỗi 
# Không phân biệt hoa/thường
print('- Kết quả kiểm tra sự tồn tại của "hồ chí minh" trong văn bản trên: ', x)
print('- Kết quả kiếm tra sự tồn tại của "non sông" trong văn bản trên: ', y)

# Tách chuỗi thành 1 danh sách
list_vanban = vanban.split('.')
print('- Tách câu trong đoạn văn: \n',list_vanban)
print('- Kiểm tra sự tồn tại của kí tự khác kí tự chữ và số trong đoạn văn trên: \n\tfalse = tồn tại \n\ttrue = không tồn tại \n\tKết quả:',vanban.isalnum())
print('- Thay thế Việt Nam = VIỆT NAM: \n', vanban.replace('Việt Nam', 'VIỆT NAM'))

