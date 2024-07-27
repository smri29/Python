try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input.")

try:
    num = int(input("Enter a nubmer: "))
    print(num)
    value = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
except ValueError:
    print("Invalid Input!")
