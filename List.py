#List and its methods
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
print(names[0])
print(names[3])
print(names[-1])
print(names[-2])
names[0]="Rose"
print(names)
print(names.pop())
print(names.index("Sam"))
names.append("Roman")
print(names)
print(names[0:3]) # range function
                  # excluding index 3.. the last range.. upto the last range
print(names[2:]) #from 2 to the last element

number = [1,2,3,4,5,6,7,8,9]
number.append(10)
print(number)
number.insert(0, 0)
number.remove(10)
print(number)
#number.clear()
#print(number)
print(1 in number)
print(10 in number)
print(len(number))

names.extend(number)
print(names)