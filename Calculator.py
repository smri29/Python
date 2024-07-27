def calculator (num1, op, num2):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by Zero."
    else:
        return "Invalid Operator!"

num1=float(input("Enter 1st number: "))
op =input("Enter the operator: ")
num2=float(input("Enter 2nd number: "))
print(calculator(num1,op,num2))
