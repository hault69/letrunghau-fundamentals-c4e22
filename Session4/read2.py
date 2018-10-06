person = {
    "name": "Hau",
    "age": 22,
}
a = input("nhap doi tuong can xem: ")
# while True:
#     print(person[a])
#     break
if a in person: #kiem tra xem 1 thu co trong mot thu khac khong (co the dunng "not in" linh hoat voi "in")
    print(person[a])
else:
    print("Not Found!!")