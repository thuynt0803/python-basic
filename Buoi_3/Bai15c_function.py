"""
    Khởi tạo một danh sách gồm các điểm thi môn “Python for Analysis and machine learning” 
    của lớp AIV_Japan01 (Điểm chữ: A, B, C, D, F). 
        1) Cho biết số sinh viên trong lớp
        2) Có bao nhiêu sinh viên phải học lại môn này (điểm F).
        3) Có bao nhiêu sinh viên có điểm từ B trở lên.
        4) Sinh viên đầu tiên và cuối cùng trong lớp đã nghỉ học, tạo một bảng điểm mới 
           và loại bỏ điểm của các sinh viên này ra khỏi danh sách điểm.
    
    YÊU CẦU: Viết hàm count_mark(): trả về số sinh viên học lại và tổng số sinh viên trong lớp với tham số truyền vào là một danh sách bảng điểm
"""

def count_mark(list_diem):
    print('The list includes test scores for "Python for Analysis and machine learning" of class AIV_Japan01: \n',list_diem)
    print('\n------------------------------------ STATISTICAL ----------------------------------')
    print('1. The number of students in the class:', len(list_diem))

    print('2. Number of students to repeat:',list_diem.count('F')) # số học sinh học lại

    x = list_diem.count('A')
    y = list_diem.count('B')
    z = x + y
    print('3. Number of students with score B or higher:', z)

    list_diem.pop()  # Xóa vị trí cuối ds
    list_diem.pop(0) # Xóa vị trí đầu ds
    print('4. Transcript after two students were eliminated: \n', list_diem)


list_diem = ['C','B','A','B','B','A','C','A','A','A','F','D','A','A','C','A','B','A','D','A','F','A','A','C','F']
count_mark(list_diem)
