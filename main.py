#class file
from tkinter.font import names


class student:
    first_name = 'John'
    last_name = 'Doe'
    gender = 'Male'
    age = 24

class person: #functions within a class are called methods
    def __init__(self, name, gender, marital_status,occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salutation(self):
        print(f"Good morning {self.name}, you are {self.gender}, and {self.marital_status}")

    def display_name(self):
        print(f"Good morning, I am {self.name} ")



#CREAT A VEHICLE CLASS AND IMPLEMENT 3 INSTANCES FROM IT
class dream_car:
    def __init__(self, type, model, year_of_manufacturing,engine_size):
        self.type = type
        self.model = model
        self.year_of_manufacturing = year_of_manufacturing
        self.engine_size = engine_size






#ASSIGNMENT - MONDAY 28 OCT
#WRITE A RECTANGLE CLASS ALLOWING A METHOD PERIMETER THAT CALCULATES THE PERIMETER OF A RECTANGLE
#AND METHOD AREA OF A RECTANGLE , ANOTHER METHOD DISPLAY THAT DISPLAYS THE LENGTH AND WIDTH OF AN INSTANCE

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)


    def area(self):
        return self.length * self.width


    def display(self):
        print(f"length: {self.length}, width: {self.width}")






#INHERITANCE
class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def display(self): #THIS METHOD CAN STILL BE INHERITED BY THE CHILD CLASSES
        return f'I am {self.name} and I earn {self.salary} KSH'





class Manager(Employee):   #CHILD OF THE EMPLOYEE
    def __init__(self, name, age, salary, gender, education_level):
        super().__init__(name, age, salary, gender) #things inheriting from the parent
        self.education_level = education_level

class Developer(Employee):   #CHILD OF THE EMPLOYEE
    def __init__(self, name, age, salary, gender, coding_language):
        super().__init__(name, age, salary, gender) #things inheriting from the parent
        self.coding_language = coding_language



class HR(Employee):   #CHILD OF THE EMPLOYEE
    def __init__(self, name, age, salary, gender, job_class):
        super().__init__(name, age, salary, gender) #things inheriting from the parent
        self.job_class = job_class

class SalaryEmployee(Employee):   #CHILD OF THE EMPLOYEE
    def __init__(self, name, age, salary,gender, weekly_salary):
        super().__init__(name, age, salary, gender) #things inheriting from the parent
        self.weekly_salary = weekly_salary

    def calc_payroll(self):
        return self.weekly_salary * 4

class HourlyEmployee(Employee):   #CHILD OF THE EMPLOYEE
    def __init__(self, name, age, salary, gender, hourly_rates):
        super().__init__(name, age, salary, gender) #things inheriting from the parent
        self.hourly_rates = hourly_rates

    def calc_payroll2(self):
        return self.hourly_rates * 8 * 5

#a child can also have a child
class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, age, salary, gender, weekly_salary, commission):
        super().__init__(name, age, salary, gender, weekly_salary)
        self.commission = commission

    def calc_commission(self):
        fixed = super().calc_payroll()





#ASSIGNMENT 29 OCT

#create a parent class bankaccount which represents a bank account with ITS RESPECTIVE ATTRIBUTES
#create a deposit method that manages the deposit actions
#create a withdrawal method which manages withdrawal actions
#create a bankfees method that applies bank fees percentage of 5% on the baLANCE IN THE ACCOUNT
#create display method to display account details

#NB: ensure the parent class has at least 2 child classes

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully. Thank You!")
        else:
            print("Please Deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. Enjoy your monies")
        else:
            print("Insufficient balance/invalid withdrawal amount.")

    def apply_bank_fees(self):
        fee = self.balance * 0.05  # 5% bank fee
        self.balance -= fee
        print(f"Bank fees of {fee} are applicable.")

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


#Current Account - CHILD1
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0, fuliza_limit=500):
        super().__init__(account_holder, account_number, balance)
        self.fuliza_limit = fuliza_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.fuliza_limit):
            self.balance -= amount
            print(f"{amount} withdrawn successfully with fuliza.")
        else:
            print("Insufficient balance and fuliza limit exceeded.")

#Savings Account -CHILD2
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to savings account.")












