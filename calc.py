w = int(input("Enter your weight :"))
h = int(input("Enter your height :"))
print("your weight is :" + str(w) + " kg")
print("your height is :" + str(h) + " sm")

bmi = round(w/((h/100)**2))

print(bmi)
n = (bmi - 20)//5
m = 6 - n
print("20" + "="*n + "I" + "="*m + "50")

