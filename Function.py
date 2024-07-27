def say_hi ():
    print("Hallo! Guten Morgen. Wie geth es ihnen?")
say_hi() #Function Calling

def inf (name, age):
    print("Hello! Good Morning. "+name+" How are you? You are "+str(age))
inf("Konika", 24)

#Return Statement
def cube (num, power):
    result = pow(num, power)
    return result
num = float(input("Enter a number: "))
power = float(input("Enter the power number: "))
print(cube(num,power))