items = ['pho','com','bun']
# print(items)
# new_item = input("enter your food: ")
# items.append(new_item) #them vao cuoi
# for i in range(len(items)):
#     print(items[i], sep=" | ")
print(*items, sep="\n")
n = int(input("nhap vi tri muon xem: "))
if n>len(items):
    print("loi")
else:
    print(items[n-1])
