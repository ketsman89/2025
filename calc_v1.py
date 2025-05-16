while True:
    print("hello! Check your BMI!")
    sex = input("Enter your sex: ")
    if sex == "q":
        break
    age = int(input("How old are you :"))
    w = int(input("Enter your weight :"))
    h = int(input("Enter your height :"))
    
    print("your weight is :" + str(w) + " kg")
    print("your height is :" + str(h) + " sm")
    
    bmi = round(w/((h/100)**2))
    
    print(bmi)
    n = (bmi - 20)//5
    m = 6 - n
    print("20" + "="*n + "I" + "="*m + "50")
    if age <= 18 and sex == "male" and bmi <= 30:
        print("You are good boy!")
    if age <= 18 and sex == "male" and bmi > 30:
        print("You are fat boy! Go to gym!")
    if age <= 18 and sex == "female" and bmi <= 30:
        print("You are good girl!")
    if age <= 18 and sex == "female" and bmi > 30:
        print("You are fat girl! Go to gym!")