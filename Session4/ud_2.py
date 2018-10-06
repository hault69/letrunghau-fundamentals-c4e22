
person = {
    "name": "Hau",
    "age": 22,
}

print(person)
while True:
    check = ["d","u"]
    a = input("enter your action: ")
    if a not in check:
        print("Error!!!! Not find Action!!")
    else:
        #d
        if a == check[0]:
            b = input("enter item del: ")
            if b in person:
                del person[b]
                print(person)
            else:
                print("Not found!!")
        #u
        if a == check[1]:
            c = input("enter key update: ")
            if c in person:
                person[c] = input("enter value update: ")
                print(person)
            else:
                print("not found update!!")
        break