items = ['com','pho','com rang']
print(items)
#update
n = int(input("muon thay o vi tri nao: "))
items[n-1] = input("nhap noi dung muon thay doi: ")
print(items)
#delete
nd = input("nhap phan muon xoa: ")
if nd.isdigit():
    nd_new = int(nd)
    if nd_new>len(items):
        print("loi")
    else:
        items.pop(nd_new-1)
        print(items)
else:
    items.remove(nd)
    print(items)