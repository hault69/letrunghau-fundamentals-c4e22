dic = {
    "cau hoi":[cau1,cau2],
    "dap an": ["a","b","c","d"]
}
question = input("ban muon tra loi cau hoi nao? ")
if question == dic["cau hoi"][0]:
    answer = input("nhap dap an: ")
    if answer == dic["dap an"][0]:
        print("dung!")
    else:
        print("sai!")