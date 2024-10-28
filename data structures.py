# how we structure data and see how we can edit or manipulate it
#LISTS
from Variablesinput import first_name

employees=["pet", "ester", "john", "smith"]
print(employees)
print(employees[3])
print(employees[1:3]) #printinting using a range
employees[3]="willy"   #changing something in the list
print(employees)

#adding something in the list
employees.append("obina")
print(employees)

#adding at a spacific position
employees.insert(0, "juli")
print(employees)

#adding more than one item
employees.extend(["juli", "ann", 'kamwana'])
print(employees)




#TUPLES - use normaal brackets
languages= ('java', "python", 'kotlin')
print(languages)
print(languages[0])
print(languages[0:2])
#you can not reassign the values in a tuple, they take the values parmanenently
#you can not do this  employees[3]="willy"   #changing something in the list




#SETS
students = {'winnie', 'omosh', 'pete', 'alex'}
print(students)
# a set does not have indexing,
# checking if a value exists in a set
if "omosh" in students:
    print("omosh exists")

if "suzanne" in students:
    print("suzanne exists")
else:
    print("not available today")

#adding a value
students.add('chalo')
print(students)

students.update(['rubeni'])
print(students)

students.remove('rubeni')
print(students)



#DICTIONARY

pupil = {
    'first_name': 'ben',
    'latst_name': 'ogash',
    'gender': 'male',
    'email': 'g@mail.com',
    'DOB':'1999'
}
print(pupil)
print(pupil['DOB'])
#adding anythingvinto the dictioray
pupil['skintone'] = 'chocolate'
print(pupil)

if "skintone" in pupil:
    print(pupil['yes he is brown'])
else:
    print('not brown')



#checking for existance of a key in a dictionary
# Dictionary with book details
book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year_published': 1960,
    'genre': 'Fiction'
}

# Check if 'author' key exists in the dictionary
if 'author' in book:
    print("Key 'author' exists in the dictionary.")
else:
    print("Key 'author' does not exist in the dictionary.")

# Check if 'publisher' key exists in the dictionary
if 'publisher' in book:
    print("Key 'publisher' exists in the dictionary.")
else:
    print("Key 'publisher' does not exist in the dictionary.")


#take 4 users age nad perform logical operations with the values

#all_adults checks if all users are 18 or older.
#any_minor checks if any of the users are younger than 18.
#all_same_age checks if all four ages are equal.
#at_least_two_above_30 uses sum() to check if at least two users are older than 30.

# Taking ages of four users as input
age1 = int(input("Enter age of User 1: "))
age2 = int(input("Enter age of User 2: "))
age3 = int(input("Enter age of User 3: "))
age4 = int(input("Enter age of User 4: "))

# Logical Operations
all_adults = age1 >= 18 and age2 >= 18 and age3 >= 18 and age4 >= 18
any_minor = age1 < 18 or age2 < 18 or age3 < 18 or age4 < 18
all_same_age = age1 == age2 == age3 == age4
at_least_two_above_30 = sum([age1 > 30, age2 > 30, age3 > 30, age4 > 30]) >= 2

# Displaying results
print("\nLogical Operations Results:")
print("All users are adults:", all_adults)
print("At least one user is a minor:", any_minor)
print("All users are of the same age:", all_same_age)
print("At least two users are older than 30:", at_least_two_above_30)











