
from main import student, person, dream_car, rectangle, Employee, Manager, Developer, HR, SalaryEmployee, HourlyEmployee, CommissionEmployee, BankAccount, SavingsAccount, CurrentAccount

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



#ASSIGNMENT - MONDAY 28 OCT
rectangle1 = rectangle(23,25)

# Displaying the length and width
rectangle1.display()

# Calculating and displaying the perimeter
print("Perimeter:", rectangle1.perimeter())

# Calculating and displaying the area
print("Area:", rectangle1.area())






employee1=Employee("benson", 25, 150000, "Male")
employee2=Employee("ben", 25, 190000, "Male")
manager1=Manager("kezzy", 23, 250000, 'female', 'PHD')
manager2=Manager("Ogash", 25, 300000, 'male', 'PHD')
developer1= Developer('keya',23, 1000000, 'lesbian', 'python')
hr1= HR('evensmkora', 40, 15000, 'male', 'f')
salaryemployee1= SalaryEmployee('job', 49, 0, 'male', 3500 )
HourlyEmployee= HourlyEmployee('ken',66, 0, 'gay', 200)
commissionemployee1= CommissionEmployee('june', 18, 0, 'lesbian', 3000, 700)


print(developer1.display)
print(HourlyEmployee.display())
print(salaryemployee1.calc_payroll())
print(HourlyEmployee.calc_payroll2())
print(commissionemployee1.calc_commission())




#ASSIGNMENT 29 OCT

#create a parent class bankaccount which represents a bank account with ITS RESPECTIVE ATTRIBUTES
#create a deposit method that manages the deposit actions
#create a withdrawal method which manages withdrawal actions
#create a bankfees method that applies bank fees percentage of 5% on the baLANCE IN THE ACCOUNT
#create display method to display account details

#NB: ensure the parent class has at least 2 child classes



savingsaccount1 = SavingsAccount("Benson Mogambi", "KENYA123", 1000)
currentaccount1 = CurrentAccount("Waka Waka", "UGANDA456", 50000)
currentaccount2 = CurrentAccount("Onyi Papa", "TZ456", 100)

print("\n--- Savings Account Details ---")
savingsaccount1.deposit(200)
savingsaccount1.add_interest()
savingsaccount1.apply_bank_fees()
savingsaccount1.display_account_details()

print("\n--- Current Account Details ---")
currentaccount1.deposit(300)  # Call the deposit method on the instance
currentaccount1.withdraw(900)
currentaccount1.apply_bank_fees()
currentaccount1.display_account_details()

print("\n--- Current Account Details ---")
currentaccount2.deposit(300)
currentaccount2.withdraw(900)
currentaccount2.apply_bank_fees()
currentaccount2.display_account_details()


