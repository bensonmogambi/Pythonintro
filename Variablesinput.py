from logging import StringTemplateStyle

print('Hello Ben')   #prints out texts - displays output to the users
print(45.099) #text goes in the '' but numbers don't

#VARIABLES - they contain/host something to be passed around in an algorithm
#first_name #this is the variable = "Benson" # this is the value
first_name = "Benson"
print(first_name)
age = 25
print(age)
print(first_name, age)

#DATA TYPES
#INTEGER - is a whole number
a = 234

#STRING - is a text
b='please fill this form'

#FLOAT - is a decimal number
c = 25.23

#BOOLEAN - true or false
is_girl = True
is_boy = False

#Input from users - allows input from the users
name = input("what is your name? ")
print(name)
age = input("what is your age? ")
print(age)
height = input("what is your height? ")
print("Your height is ", height+ "inches tall")
print("My name is ", name+ ", I am ", age+ " years old", "my height is ", height+ "inches tall")

#TYPE CONVERSIONS
first_number = input("please enter your first number: ")
second_number = input("please enter your second number: ")
sum = int(first_number) + int(second_number)
print(sum)

age1 = int(input("please enter your age: "))
age2 = int(input("please enter your age: "))
subtract = age1 - age2
print("Your age is difrence is ",subtract)

x= float(input("first mark: "))
y= float(input("second mark: "))
diff = x- y
print(diff)


#TAKE IN A PERSONS WEIGHT AND HIGHT THE CALCULATE THEIR BMI AND DISPLAY THEIR BMI
weight = float(input("please enter your weight in kg: "))
height = float(input("please enter your height in meters: "))
BMI = weight/height
print("My BMI is ", BMI)


















