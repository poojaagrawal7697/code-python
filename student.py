student_name = input("Enter student name : ")
student_age = int(input("Enter student age : "))

print("Student name is {0} and Student age is {1}".format(student_name,student_age))        #.format
print(f"Student name is {student_name} and Student age is {student_age}")
print("Student name is ",student_name,"and Student age is",student_age)

print(type(student_name) == type("dummy string"))
print(type(student_age))

if student_age >= 18 and student_age <=25:
    print("above 18")
elif student_age >= 26 and student_age <=45:
    print("Above 25")
else:
    print("Bro too old.")

#print("Above 18")
