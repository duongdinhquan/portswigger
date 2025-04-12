with open("D:\\down chome\\tài liệuk\\Pentest\\portswigger\\list_username.txt" , "w") as f:
    for i in range(1,151):
        f.write("carlos\n")
        if i % 2==0:
            f.write("wiener\n") 