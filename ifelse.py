#if statements
temperature = int(input("Enter today's Temperature: "))
if temperature>30:
    print("It's a hot day. Drink plenty of water.")
elif temperature >20: #(20<temp<30)
    print("It's a nice day.")
elif temperature >10: #(10<temperature<20)
    print("It's a bit cold.")
else:
    print("It's cold. Wear warm clothes.9")

def max_num (num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3
print(max_num(40,50,60))
