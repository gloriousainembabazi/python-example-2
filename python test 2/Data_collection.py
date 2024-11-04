#DATA
#Creating a list
student_name =("Brenda",'charity','Glorious','faith','Agnes')# strings
student_marks =(90,50,60,55,70)
student_data ="Glorious",60,'kamwokya'#mixed types

#first item
print(student_name[1])#second item
print(student_name[2])#third item
print(student_name[3])#fourth item
print(student_name[4])#accessing list of items

#indexes (positive indexing)
print(student_name[0])#last item

#indexes (negative indexing)
print(student_name[-5])#last item
print(student_name[-4])#fourth item
print(student_name[-3])#third item
print(student_name[-2])#second item
print(student_name[-1])#first item

# adding an item to the existing lists

student_name.insert(2,'Mery')
print(student_name)

#add at the end
student_name.append('joviah')
print(student_name)