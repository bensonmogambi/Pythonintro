#key word that identifies a function is def, they are supposed to return results not print
from Variablesinput import first_name


def my_function():
    print('good morning andy')
    #if i want multiple prints
    print('good morning pete')
    print('good morning kezzy')
    print('good morning andy1')

my_function() #you must do this to call out tje function
#if i want them doubled i call them here again
my_function()
my_function()



#functions do take variables
def my_string():
    hello= 'hello kezzy, i miss you'
    print(hello)

my_string()


#functionc can take arguements or parameters
def arg(name):
    print(name)

arg('kezzy')
arg('benny')
arg('leah')

def my_func(first_name):
    print('Hello ' + first_name + ' please come home')
    print(f'FirstName : {first_name} ')  #f stands for the factor name#

my_func('kezzy')


def my_func2(first_name, age):
    print(f'Hello  {first_name} your age is {age} years old')

my_func2(first_name= 'kezzy' , age= 23)
my_func2(first_name= 'benny' , age= 25)


def my_func3(first_name, last_name, age):
    print(f'Hello  {first_name} {last_name}your age is {age} years old')

my_func3(first_name = "kezzy", last_name='keya', age= 23)



#creat a function that takes two numbers as arguments and performs a summation then displays the summation

def add_numbers(num1, num2):
    summation = num1 + num2
    print(summation)
    print(f'the summation of {num1} and {num2} is {summation}')

add_numbers(5, 35)

def multiply(a ,b):
    result = a * b
    return result

print(multiply(10,20))

#function that takes your current age and desplays your age in the next 8yrs

def age_calc(current_age):
    new_age = current_age + 8
    return new_age
print(age_calc(24))


# adding conditional statements

def promotion(name, age):
    if age >= 5 and age <= 7:
        return f'{name} you are {age}yrs old and you are promoted to grade 3'
    elif age == 8:
        return f'{name} you are {age}yrs old you are promoted to grade 4'
    elif age >8 and age <= 10:
        return f'{name} you are {age}yrs old you are promoted to grade 5'
    else:
        return f'{name} you are not supposed to be in lower primary'

print(promotion('kezzy', 8))
print(promotion('benny', 11))


# creat a function called greet that takes a persons name as an argument and returns a greeting message.
# if the name is 'Kezzy' or 'Ben' it returns a personalized greeting
# for any other name it should return a general greeting

def greet(name):
    if name == 'Kezzy':
        return "Hello Kezzy! I miss you"
    elif name == 'Ben':
        return "Hello Ben! Hope you're having a wonderful day!"
    else:
        return f'Hello, {name}  wassup!'

print(greet('Kezzy'))
print(greet('Ben'))
print(greet('Alice'))

#write a programm that finds a maximum of three numbers
def find_maximum(num1, num2, num3):
    maximum = num1  # Assume the first number is the largest
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    return maximum

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

print(f"The maximum of {number1}, {number2}, and {number3} is {find_maximum(number1, number2, number3)}")

#creat a python func tat sums all numbers in a list
def sum_of_list(numbers):
    total = sum(numbers)  # Use the built-in sum() function to add up all numbers
    return total

numbers = [1, 2, 3, 4, 5]
print("The sum of the list is:", sum_of_list(numbers))















