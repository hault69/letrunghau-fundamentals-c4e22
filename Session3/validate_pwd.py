while True:
    pwd = input(" enter pass: ")
    if len(pwd) <8:
        print("not enough!")
    elif pwd.isdigit():
        print("toan so")
    elif pwd.isupper():
        print(" toan chu hoa")
    elif pwd.islower():
        print("toan chu thuong")
    else:
        print("ok")
        break