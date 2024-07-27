#simple weight converter using if else statements

Weight = float(input("Enter your weight: "))
Unit = input("(K)g or (L)bs: ")
if Unit.upper() == "K":
    converted=Weight/0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = Weight*0.45
    print("Weight in Kg: " + str(converted))
