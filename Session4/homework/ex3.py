quiz = {
    "question": "if x =8, then what is the value of 4(x+3)? ",
    "choices": ["1. 35","2. 36","3. 40","4. 44"],
    "right choice": 3 
}
while True:
    print(quiz["question"])
    for i in quiz["choices"]:
        print(i)
    a = int(input("your choice: "))
    if a>4:
        print("loi")
    else:
        if a == quiz["right choice"]:
            print("Bingo")
            break
        else:
            print(":(") 