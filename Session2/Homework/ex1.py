h= int(input(" your height(cm): "))
weight= int(input(" your weight(kg): "))
height=h/100
BMI = weight/(height*height)
print(BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")