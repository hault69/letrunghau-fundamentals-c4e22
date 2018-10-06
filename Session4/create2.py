person = {
    "Name": "Hau"
}
print(person)

text = input("Add new items: ")
pair = text.split(",") #tách các phần tử cách nhau bởi dấu "," thành list các phần tử
# new_key = pair[0]
# new_value = pair[1]
new_key,new_value = pair #mảng bên phải phải luôn có giá trị nhiều hơn bên trái
person[new_key] = new_value
print(person)