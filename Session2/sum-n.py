n = 0
a = int(input("nhap a: "))
for i in range(a+1):
    n=n+i
print("day so sau: ", *range(a+1))
print("co sum = ",n)
