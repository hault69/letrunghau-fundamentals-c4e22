sheep = [5, 7, 300, 90, 24, 50, 75]

for u in range(3):
    print("month: ", u+1)
    #2_1
    print("Hello, my name is Hau and these are my ship sizes: 0",*sheep, sep = ", ")
    #2_2
    i = 0
    bz = 0
    while i<7:
        a = int(sheep[i])
        if bz<a:
            bz = a
        i+=1
    print("Now my biggest sheep has size",bz,"let's shear it")
    #2_3
    index = sheep.index(bz)
    sheep[index] = 8
    print("After sheep: ", *sheep)
    #2_4
    for n in range(len(sheep)):
        sheep[n] += 50
    print("Grow up sheep: ",*sheep)
    #2_6
    sum=0
    for m in sheep:
        sum = sum + m
    total = sum*2
    print("Total: ",total,"$")