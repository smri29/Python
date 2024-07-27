from objectFunction import Student
Student1=Student("Osman", "Business", 3.43)
Student2=Student("Faria", "Arts", 3.84)
Student3=Student("Ridoy", "Designing", 3.76)

print(Student1)
print("Honor Roll: "+str(Student1.on_honor_roll()))
print(Student2)
print("Honor Roll: "+str(Student2.on_honor_roll()))
print(Student3)
print("Honor Roll: "+str(Student3.on_honor_roll()))
