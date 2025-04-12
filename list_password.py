with open("D:\\down chome\\tài liệuk\\Pentest\\portswigger\\123456.txt", "r") as f:
    lines = f.read().split("\n")
# tạo ra một list chứa full đòng cảu file

new_lines = [] # chứa các dòng mới

j=0
for line in lines :
    new_lines.append(line)
    j+= 1
    if j%2 == 0:
        new_lines.append("peter") # thêm dòng "peter" vào sau mỗi dòng chẵn

with open("D:\\down chome\\tài liệuk\\Pentest\\portswigger\\list_password.py.txt" ,"w") as f:
    f.write('\n'.join(new_lines))
    
                          