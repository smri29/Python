numbers = [1,2,3,4,5,6]
print(numbers)
for item in numbers:
    print(item)

i=0
while i<len(numbers):
    print(numbers[i])
    i=i+1

#The Range Fucntion-- to generate a sequence of numbers
print("Range Fucntion: ")
numbers = range(5)
print(numbers)
for number in numbers:
    print(number)
print("jumping or incrementing in range fucntion: ")
#to jump/increment numbers or range by 2 or 3 or 5
numbers = range(2,10,2)
for number in numbers:
    print(number)
print("We can write directly in the For Loop: ")
for item in range(5):
    print(item)
print("directly incrementing or jumping: ")
for item in range(2,20,4):
    print(item)

names = ["Jey","Jimmy","Roman","Paul","Jacob"]
for name in range(len(names)):
    print(names[name])
