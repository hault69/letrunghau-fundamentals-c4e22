while True:
    items = ['T-Shirt', 'Sweater']
    a = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    check = ['c','r','u','d']
    #r
    if a==check[1]:
        print(*items, sep=" , ")
    #c
    if a==check[0]:
        b = input("enter new item: ")
        items.append(b)
        print(*items, sep=", ")
        new_items = items
    #u
    if a==check[2]:
        c = int(input("nhap vi tri muon update: "))
        if (c)>len(new_items):
            print('loi')
        else:
            new_items[c-1] = input("nhap noi dung muon thay doi: ")
            print(*new_items, sep=", ")

    #d
    if a == check[3]:
        nd = input("nhap phan muon xoa: ")
        if nd.isdigit():
            nd_new = int(nd)
            if nd_new>len(new_items):
                print("loi")
            else:
                new_items.pop(nd_new-1)
                print(*new_items, sep=", ")
        else:
            new_items.remove(nd)
            print(*new_items, sep=", ")
        break