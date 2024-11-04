# example
#create a function that returns the main components of a functions in python.

def function_basics():
    print(f"The main components of functions are:\n fuction body\n fuction parameter")
function_basics()

#create a function that returns your name,registration number and age.

def student_information():
    student_name ="Glorious"# local variables
    student_registration_number ="2024/DSC/004/SS"# local variables
    print("My name is {student_name} my registration number is {student_registration_number} and am {student_age}")

    #create a fuction that returns your student name,registration number and student age as parameters.
    
    def student_details(name,age,reg_no):
        print(f"{name},{age},{reg_no}")

        student_details("Glorious","23",'2024/DSC/004/SS')

        #RETURN VALUES
        #it also works as a print function.

        def my_name():
            return "Glorious"
        my_name()

        #or
        def her_name(name):...
        her_name("charity")
        def my_age():
            age=23
            return age
        print(f"my name is {'my_name_approach'}")

        #create a fuction that calculate the area of a triangle.
        #the base and height must be fuction parameters.
        def area_of_triangle(base,height):
            print(f"The area of a triangle of base:{base} and height: {height} is {area_of_triangle}")
            area_of_triangle(3,5)

            #approach

        def area_of_triangle():
            base = int(input("Enter the base of a triangle:"))
            height =int(input("Enter the height of a triangle:"))
            area = int(1/2*base*height)
            print(f"The area of a triangle with base:{base} and height:{height} is {area}")
            area_of_triangle


