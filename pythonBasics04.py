#Arithmetic Operators
print("Arithmetic Operators: ")
x = 10
print(x+3) #addition
print(x-3) #subtraction
print(x*3) #multiplication
print(x/3) #division
print(x//3) #only the integer part of the division result
print(x%3) #modulus (returns the remainder)
print(x**3) #returns the exponential like 10^3 (power)
print(x)
x+=7 #adds 7 to 10
x-=3 #subtracts 3 from 17
x*=2 #multiplys 2 to 14
x/=2 #divides 2 from 28
print(x)

#Operator Precendendce
print("Operator Precedence: ")
z=10+3*2-6
print(z)
zz=(10+3)*2-6 #by using the parenthesis we can change the precedence of operators
print(zz)

#Comparison Operators
print("Comparison Operators:")
r=10>2
print(r)

#greater than (>)
#greater than or equal to (>=)
#less than (<)
#less than or equal to (<=)
#equal to (==)
#no equal to (!=)

#Logical Operators
print("Logical Operators:")
price = 25
print(price >10 and price <30)
price = 5
print(price>10 or price<30)
print(not price >10)
#and - (both)
#or - (at least one)
#not - (inverses any value that we give in)