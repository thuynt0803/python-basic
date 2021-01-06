"""
    XÁC ĐỊNH MÙA TRONG NĂM: Nhập vào tháng sinh của bạn và cho tiết bạn sinh vào mùa nào?
    Yêu cầu:
        . Nếu 1, 2, 3: Bạn sinh vào Mùa xuân
        . Nếu 4, 5, 6: Bạn sinh vào Mùa hạ
        . Nếu 7, 8, 9: Bạn sinh vào Mùa thu
        . Nếu 10, 11, 12: Bạn sinh vào Mùa đông
        . <1 hoặc >12: Tháng sinh nhập vào không đúng
"""
thangsinh = int(input('Tháng sinh: '))
if (1 <= thangsinh <= 12):
     if(1 <= thangsinh <= 3): print('Bạn sinh vào mùa Xuân')
     elif (4 <= thangsinh <= 6): print('Bạn sinh vào mùa Hạ')
     elif (7 <= thangsinh <= 9): print('Bạn sinh vào mùa Thu')
     else: print('Bạn sinh vào mùa Đông')
else: print('Tháng sinh được nhập không hợp lệ!')

    
