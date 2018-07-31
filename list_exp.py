fruits = ["mangoes", "oranges", "pear"]

student1 = {
    "name": "lama", "age": 17, "math_grade": 98
}

student2 = {
    "name": "precious", "age": 16, "math_grade": 97
}

student3 = {
    "name": "michele", "age": 15, "math_grade": 96
}
#iterate a list
#for variable_name in listname:
    # do something


#print every fruit in the fruits list
for fruit in fruits:
    print(fruit)

    #print the age student 1
print(student1["age"])

    #print the name student 2
print(student2["name"])

    #print the math grade student 3
print(student3["math_grade"])


students = [student1, student2, student3]
#print list of students
print(students)


#print each student dicitionary in students list
for student in students:
    print(student)

#print each student's math_grade
for math_grade in students:
    print()
