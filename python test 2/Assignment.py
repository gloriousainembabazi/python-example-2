#question 1
#Given the two lists below,

student_names =['sandra','patricia','phionah','Anitah']
student_marks =[80,50,78,95]
data =['sandra',80,'kamwokya']
print(student_names)

# 1 (a) a list that excludes the first and last items.

print(student_names[1:3])

# 1 (b) patricia,faith,phionah,Anitah.
student_names = ['patricia', 'faith', 'phionah', 'Anitah']
print(student_names)

# 1 (c) add Masha at the 4th position.
student_names.insert(4,'Masha')
print(student_names)

# 1 (d) update the name phionah ensure the name is stored as phionah Alladina.

student_names.append("phionah Aladinah")
print(student_names)

student_names.remove("phionah")
print(student_names)

# 1 (e) displa the length of the student_list.

student_names =['sandra','patricia','phionah','Anitah']
list_length =len(student_names)
print(list_length)

# 1 (f) print all student_names using a for loop.
student_name = ['sandra', 'patricia', 'phionah', 'Anitah']
for name in student_name:
    print(name)


# 1 (g) calculate the total marks of the student_marks variable.
student_marks = [80, 50, 78, 95]
total_marks = sum(student_marks)
print(total_marks)