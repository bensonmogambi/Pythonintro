from main import student, person, dream_car

student1 = student()
print(student1.first_name)
print(student1.last_name)
print(student1.age)
print(student1.gender)

person1= person(name='jon', gender="female", marital_status='single',occupation='software engineer')
person2= person(name='ben', gender="male", marital_status='married',occupation='software engineer')
person3= person(name='treva', gender="male", marital_status='complicated',occupation='chef')
print(person1.name)
print(person3.name)
print(person3.marital_status)
print(f'Name:{person1.name}, Gender:{person1.gender}, Marital_status:{person1.marital_status}, Occupation:{person1.occupation}')

#passing the object salutation
person1.salutation()
person3.salutation()

person2.display_name()
person3.display_name()
person1.display_name()



#instances of the Vehicle class
vehicle1 = dream_car(type='Car', model='Toyota Camry', year_of_manufacturing=2020, engine_size='2.5L')
vehicle2 = dream_car(type='Motorcycle', model='Honda CBR', year_of_manufacturing=2019, engine_size='1.0L')
vehicle3 = dream_car(type='Truck', model='Ford F-150', year_of_manufacturing=2021, engine_size='3.5L')
#information about each vehicle
print(f'Vehicle Type: {vehicle1.type}, Model: {vehicle1.model}, Year: {vehicle1.year_of_manufacturing}, Engine Size: {vehicle1.engine_size}')
print(f'Vehicle Type: {vehicle2.type}, Model: {vehicle2.model}, Year: {vehicle2.year_of_manufacturing}, Engine Size: {vehicle2.engine_size}')
print(f'Vehicle Type: {vehicle3.type}, Model: {vehicle3.model}, Year: {vehicle3.year_of_manufacturing}, Engine Size: {vehicle3.engine_size}')




